import json
import os

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
            .level-header { background: linear-gradient(135deg, #6c5ce7, #a29bfe); color: #fff; padding: 12px 24px; border-radius: 8px; font-size: 1.6em; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.08); }
            
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
    if os.path.exists("data_raw/vocab_master_enriched.json"):
        with open("data_raw/vocab_master_enriched.json", "r", encoding="utf-8") as f:
            vocab = json.load(f)
        generate_v2_html(vocab)
    else:
        print("No enriched data found.")
