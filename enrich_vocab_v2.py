import json
import bz2
import csv
import re
import requests
import concurrent.futures
import time
import sys

import os
import getpass

# Default to empty or load from env
USER_KEY = os.environ.get("YAHOO_APP_ID", "")

def get_user_key():
    global USER_KEY
    if USER_KEY:
        return USER_KEY
    
    print("\n" + "="*50)
    print("Please enter your Yahoo Japan Client ID (App ID).")
    print("You can get one at: https://e.developer.yahoo.co.jp/dashboard/")
    print("Leave empty to skip API enrichment and just generate HTML from existing data.")
    print("="*50 + "\n")
    
    key = input("Yahoo App ID: ").strip()
    USER_KEY = key
    return key

    # Remove （...）, (~...), etc.
    # remove trailing ~
    w = re.sub(r'（.*?）', '', word)
    w = re.sub(r'\(.*?\)', '', w)
    w = w.replace('～', '').replace('~', '')
    w = w.strip()
    return w

def get_yahoo_furigana(word, client_id):
    headers = {
        "User-Agent": f"Yahoo AppID: {client_id}",
        "Content-Type": "application/json"
    }
    payload = {
        "id": "12345",
        "jsonrpc": "2.0",
        "method": "jlp.furiganaservice.furigana",
        "params": {
            "q": word,
            "grade": 1
        }
    }
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            resp = requests.post(YAHOO_API_URL, headers=headers, json=payload, timeout=10)
            if resp.status_code == 200:
                t = resp.json()
                if 'error' in t: # Yahoo sometimes returns 200 with error
                     print(f"Yahoo API Error for {word}: {t['error']}")
                     if 'Rate limit' in str(t['error']) or '利用制限' in str(t['error']):
                         time.sleep(60)
                         continue
                     return None
                return t
            elif resp.status_code == 429:
                print(f"Rate limit hit for {word}. Sleeping 60s...")
                time.sleep(60)
                continue
            else:
                print(f"Error {resp.status_code} for {word}")
                return None
        except Exception as e:
            print(f"Exception for {word}: {e}")
            time.sleep(5)
            
    return None

def parse_yahoo_result(result, original_word):
    # Extract ruby html
    try:
        word_list = result['result']['word']
        html_str = ""
        for w in word_list:
            if 'subword' in w:
                for sw in w['subword']:
                    if 'furigana' in sw and sw['furigana'] != sw['surface']:
                         html_str += f"<ruby>{sw['surface']}<rt>{sw['furigana']}</rt></ruby>"
                    else:
                        html_str += sw['surface']
            else:
                if 'furigana' in w and w['furigana'] != w['surface']:
                    html_str += f"<ruby>{w['surface']}<rt>{w['furigana']}</rt></ruby>"
                else:
                    html_str += w['surface']
        return html_str
    except:
        return original_word




def process_enrichment():
    # Check if enriched exists to skip API
    try:
        with open("data_raw/vocab_master_enriched.json", "r", encoding="utf-8") as f:
            print("Found existing enriched data. Skipping API calls...")
            enriched_vocab = json.load(f)
            generate_v2_html(enriched_vocab)
            return
    except FileNotFoundError:
        pass

    # Load Master
    try:
        with open("data_raw/vocab_master.json", "r", encoding="utf-8") as f:
            vocab = json.load(f)
    except:
        print("No master json")
        return

    # Load Sentences
    print("Loading sentences...")
    sentences = []
    try:
        with bz2.open("jpn_sentences.tsv.bz2", "rt", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                if len(row) >= 3 and row[1] == 'jpn':
                    sentences.append(row[2])
    except FileNotFoundError:
        print("Warning: jpn_sentences.tsv.bz2 not found. Examples finding will be skipped.")

    print(f"Loaded {len(sentences)} sentences.")
    
    # 1. Improved Matching
    print("Matching examples...")
    needed_words_map = {clean_word(w['word']): w['id'] for w in vocab}
    examples = {}
    
    count = 0
    start_len = len(needed_words_map)
    
    for s in sentences:
        if len(s) > 80: continue # Prefer shorter examples
        
        found = []
        for w, wid in needed_words_map.items():
            if len(w) < 2: 
                if w in ['目', '手', 'き', 'え']: pass
            
            if w in s:
                examples[wid] = s
                found.append(w)
        
        for w in found:
            del needed_words_map[w]
            
        if not needed_words_map: break
        
        count += 1
        if count % 50000 == 0:
            print(f"Scanned {count} sentences. Found {start_len - len(needed_words_map)} examples.")

    print(f"Total Examples Found: {len(examples)}/{len(vocab)}")
    
    # 2. Yahoo API (Parallel)
    client_id = get_user_key()
    
    if not client_id:
        print("No Yahoo App ID provided. Skipping new API calls.")
        print("Generating HTML from existing progress and raw data...")
        
        # Load whatever progress we have
        enriched_map = {}
        if os.path.exists("data_raw/vocab_master_enriched.json"):
             with open("data_raw/vocab_master_enriched.json", "r", encoding="utf-8") as f:
                existing = json.load(f)
                for item in existing:
                    enriched_map[item['id']] = item
        
        # Combine and generate
        final_vocab = []
        for v in vocab:
             if v['id'] in enriched_map:
                 final_vocab.append(enriched_map[v['id']])
             else:
                 # Default logic for raw items
                 v['ruby_html'] = v['word']
                 v['example'] = examples.get(v['id'], "No example available.")
                 final_vocab.append(v)
        
        final_vocab.sort(key=lambda x: (x.get('level',''), x.get('id','')))
        generate_v2_html(final_vocab)
        return

    print("Fetching Precise Furigana (Yahoo)...")
    CLIENT_ID = client_id
    
    # Load existing progress if any
    enriched_map = {}
    try:
        with open("data_raw/vocab_master_enriched.json", "r", encoding="utf-8") as f:
            existing = json.load(f)
            for item in existing:
                enriched_map[item['id']] = item
        print(f"Loaded {len(enriched_map)} existing items from progress.")
    except FileNotFoundError:
        print("No existing progress found. Starting fresh.")

    # Identify what needs processing
    to_process = []
    for item in vocab:
        # Check if already processed and has valid ruby (heuristic: ruby_html != word, or manually checked)
        # Actually simplest is: if in enriched_map, we assume it's done unless we force retry.
        # But we want to retry if it was a fallback? 
        # For now, let's assume if it exists in enriched_map, it's done.
        # EXCEPT if we want to fill usage...
        # Let's just update the example matching regardless, but skip API.
        
        if item['id'] in enriched_map and 'ruby_html' in enriched_map[item['id']]:
            # Update example just in case matching logic changed
            enriched_map[item['id']]['example'] = examples.get(item['id'], "No example available.")
            continue
        
        to_process.append(item)
    
    print(f"Items to process with API: {len(to_process)}")
    
    # Function to save progress
    def save_progress():
        # Reconstruct full list based on vocab order
        full_list = []
        for v in vocab:
            if v['id'] in enriched_map:
                full_list.append(enriched_map[v['id']])
            else:
                # Not processed yet, use raw
                full_list.append(v)
        
        full_list.sort(key=lambda x: (x.get('level',''), x.get('id','')))
        with open("data_raw/vocab_master_enriched.json", "w", encoding="utf-8") as f:
            json.dump(full_list, f, ensure_ascii=False, indent=2)
        print("Progress saved.")

    if to_process:
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future_to_item = {executor.submit(get_yahoo_furigana, item['word'], CLIENT_ID): item for item in to_process}
            
            completed = 0
            for future in concurrent.futures.as_completed(future_to_item):
                item = future_to_item[future]
                try:
                    data = future.result()
                    if data:
                        item['ruby_html'] = parse_yahoo_result(data, item['word'])
                    else:
                        item['ruby_html'] = item['word'] # Fallback
                except:
                    item['ruby_html'] = item['word']
                
                # Attach example
                item['example'] = examples.get(item['id'], "No example available.")
                
                # Update map
                enriched_map[item['id']] = item
                
                completed += 1
                if completed % 20 == 0:
                    print(f"Processed API {completed}/{len(to_process)}")
                    if completed % 50 == 0:
                        save_progress()
        
        # Save final
        save_progress()
    else:
        print("All items already enriched.")
        # Just ensure examples are updated and HTML generated
        save_progress()

    # Determine final list for HTML generation
    final_vocab = []
    for v in vocab:
         if v['id'] in enriched_map:
             final_vocab.append(enriched_map[v['id']])
         else:
             final_vocab.append(v)
    final_vocab.sort(key=lambda x: (x.get('level',''), x.get('id','')))
    
    # Generate V2 HTML
    generate_v2_html(final_vocab)

def generate_v2_html(vocab):
    html_content = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>JLPT Vocabulary N5-N1 (Enhanced)</title>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <style>
            body { font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif; background: #f8f9fa; color: #333; margin: 0; padding: 20px; }
            .container { max-width: 1100px; margin: 0 auto; background: #fff; padding: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-radius: 12px; }
            h1 { text-align: center; color: #2c3e50; margin-bottom: 30px; }
            
            /* API Key Input */
            .settings-panel { background: #eef2f7; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center; gap: 10px; }
            .settings-panel input { flex: 1; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
            
            .level-section { margin-bottom: 50px; }
            .level-header { background: linear-gradient(135deg, #6c5ce7, #a29bfe); color: #fff; padding: 12px 24px; border-radius: 8px; font-size: 1.6em; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            
            table { width: 100%; border-collapse: separate; border-spacing: 0; }
            th { text-align: left; padding: 15px; background: #f1f3f5; color: #495057; font-weight: 600; border-bottom: 2px solid #dee2e6; }
            td { padding: 15px; border-bottom: 1px solid #e9ecef; vertical-align: middle; }
            tr:last-child td { border-bottom: none; }
            tr:hover { background-color: #f8f9fa; }
            
            /* Ruby Styles */
            ruby { font-size: 1.25em; font-weight: 500; }
            rt { font-size: 0.6em; color: #868e96; }
            
            .meanings .cn { font-weight: bold; font-size: 1.05em; color: #212529; margin-bottom: 4px; }
            .meanings .en { font-size: 0.9em; color: #868e96; }
            
            .example-box { display: flex; align-items: flex-start; gap: 8px; margin-top: 5px; }
            .example-text { font-size: 0.95em; color: #495057; background: #e7f5ff; padding: 8px 12px; border-radius: 6px; line-height: 1.5; flex: 1; }
            .play-btn { 
                background: none; border: none; cursor: pointer; color: #228be6; 
                padding: 4px; border-radius: 50%; transition: background 0.2s;
                opacity: 0.7;
                display: flex; align-items: center; justify-content: center;
            }
            .play-btn:hover { background: #d0ebff; opacity: 1; }
            .word-play-btn { color: #868e96; margin-right: 5px; transform: scale(0.9); }
            .word-play-btn:hover { color: #228be6; background: none; }
            
        </style>
        <script>
            let googleApiKey = localStorage.getItem('google_tts_key') || '';
            
            function saveKey() {
                const input = document.getElementById('api-key-input');
                googleApiKey = input.value.trim();
                localStorage.setItem('google_tts_key', googleApiKey);
                alert('API Key Saved!');
            }
            
            async function playAudio(text) {
                if (!googleApiKey) {
                    alert('Please enter your Google Cloud API Key at the top of the page to use TTS.');
                    return;
                }
                
                const url = `https://texttospeech.googleapis.com/v1/text:synthesize?key=${googleApiKey}`;
                const data = {
                    input: { text: text },
                    voice: { languageCode: 'ja-JP', ssmlGender: 'NEUTRAL' },
                    audioConfig: { audioEncoding: 'MP3' }
                };
                
                try {
                    const response = await fetch(url, {
                        method: 'POST',
                        body: JSON.stringify(data)
                    });
                    const result = await response.json();
                    if (result.audioContent) {
                        const audio = new Audio("data:audio/mp3;base64," + result.audioContent);
                        audio.play();
                    } else {
                        console.error(result);
                        alert('TTS Error: ' + (result.error ? result.error.message : 'Unknown error'));
                    }
                } catch (e) {
                    alert('Network Error: ' + e.message);
                }
            }
            
            window.onload = function() {
                const input = document.getElementById('api-key-input');
                if(input) input.value = googleApiKey;
            }
        </script>
    </head>
    <body>
        <div class="container">
            <h1>日本語単語帳 N5-N1</h1>
            
            <div class="settings-panel">
                <label for="api-key-input">Google Cloud API Key (for TTS):</label>
                <input type="password" id="api-key-input" placeholder="Enter your API Key here">
                <button onclick="saveKey()" style="background:#5c7cfa; color:white; border:none; padding:8px 16px; border-radius:4px; cursor:pointer;">Save</button>
            </div>
    """
    
    words_by_level = {"N1": [], "N2": [], "N3": [], "N4": [], "N5": []}
    for entry in vocab:
        lvl = entry.get("level", "Uncategorized")
        if lvl in words_by_level:
            words_by_level[lvl].append(entry)
            
    for lvl in ["N5", "N4", "N3", "N2", "N1"]:
        words = words_by_level[lvl]
        if not words: continue
        
        html_content += f'<div class="level-section"><div class="level-header">{lvl} ({len(words)} Words)</div>'
        html_content += '<table><thead><tr><th style="width:5%">#</th><th style="width:25%">Word</th><th style="width:30%">Meaning</th><th style="width:40%">Example</th></tr></thead><tbody>'
        
        for i, w in enumerate(words):
            # Use enriched Ruby HTML
            word_html = w.get('ruby_html', w['word'])
            word_raw = w['word']
            
            cn = w['meaning_cn']
            en = ", ".join(w['meaning_en'][:2]) if w.get('meaning_en') else ""
            ex = w.get('example', 'No example.')
            
            # Escape quotes for JS
            word_js = word_raw.replace("'", "\\'").replace('"', '&quot;')
            ex_js = ex.replace("'", "\\'").replace('"', '&quot;')
            
            play_btn = ""
            if ex and ex != 'No example.' and ex != 'No example available.':
                play_btn = f'<button class="play-btn" onclick="playAudio(\'{ex_js}\')"><i class="material-icons">volume_up</i></button>'
            
            word_play_btn = f'<button class="play-btn word-play-btn" onclick="playAudio(\'{word_js}\')" title="Play Word"><i class="material-icons">volume_up</i></button>'

            html_content += f"""
            <tr>
                <td style="color:#adb5bd; font-weight:bold;">{i + 1}</td>
                <td>
                    <div style="display:flex; align-items:center;">
                        {word_play_btn}
                        <div>{word_html}</div>
                    </div>
                </td>
                <td class="meanings">
                    <div class="cn">{cn}</div>
                    <div class="en">{en}</div>
                </td>
                <td>
                    <div class="example-box">
                        {play_btn}
                        <div class="example-text">{ex}</div>
                    </div>
                </td>
            </tr>
            """
        html_content += '</tbody></table></div>'

    html_content += "</div></body></html>"
    
    with open("vocab_master_v2.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Saved vocab_master_v2.html")

if __name__ == "__main__":
    process_enrichment()
