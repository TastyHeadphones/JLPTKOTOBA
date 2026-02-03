import json
import bz2
import csv
import re
import html

def load_sentences(filepath):
    print("Loading sentences from TSV...")
    sentences = []
    try:
        with bz2.open(filepath, "rt", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                if len(row) >= 3:
                     # ID, Lang, Text
                     if row[1] == 'jpn':
                         sentences.append(row[2])
    except Exception as e:
        print(f"Error loading sentences: {e}")
    print(f"Loaded {len(sentences)} sentences.")
    return sentences

def match_sentences(words, sentences):
    print("Matching sentences to words...")
    # This is O(N*M) naive, very slow. 5000 words * 200k sentences = 1 billion ops.
    # We need an index.
    
    # Actually, let's create a simplified index?
    # No, we can't index substring search easily.
    # But we can iterate sentences ONCE and check all words?
    # Sentences are many, Words are few (5000).
    # 5300 words.
    # Identify unique Kanji words vs Kana words.
    
    # Optimization:
    # Create a set of words we need.
    needed_words = {w['word']: w['id'] for w in words}
    
    # Store 1 example per word ID
    examples = {} 
    
    count = 0
    for s in sentences:
        if len(s) > 100: continue # Skip long sentences
        
        # Check against all needed words? Still slow.
        # But most words are 2+ chars.
        
        # Better: Iterate all words and use `s` as context?
        # No.
        
        # Fastest "Simple" way in python for 5000 words?
        # Aho-Corasick algorithm?
        # Or just brute force with checks?
        # 5000 words is small enough if we check "if word in s" ?
        # But we iterate 200,000 sentences.
        # 5000 * 200,000 = 1,000,000,000 char comparisons. might take 5-10 mins in pure python.
        
        # Let's try to limit number of sentences we check?
        # Or just accept it takes a minute.
        
        found_for_this_sentence = []
        for word, wid in needed_words.items():
            if wid in examples: continue # Already found one
            if word in s:
                examples[wid] = s
                # Don't break, maybe this sentence works for multiple words?
                # Actually if we found example for this word, we can remove from `needed_words` to speed up?
                found_for_this_sentence.append(word)
        
        # Remove found words significantly speeds up future iterations
        for word in found_for_this_sentence:
            del needed_words[word]
            
        if not needed_words:
            break
            
        count += 1
        if count % 10000 == 0:
            print(f"Scanned {count} sentences. Remaining words: {len(needed_words)}")

    return examples

def generate_ruby_html(word, reading):
    """
    Directly converts Word + Reading to <ruby> format.
    Simple heuristic: if Reading provided, put it on top.
    Ideally we match Kanji to Kana, but simple full-word ruby is safer for raw data.
    e.g. <ruby>漢字<rt>かんじ</rt></ruby>
    """
    if not reading or reading == word:
        return word
    
    # If no Kanji in word (only Kana), usually no ruby needed, but PDF format had reading?
    # If reading == word, return word.
    
    return f"<ruby>{word}<rt>{reading}</rt></ruby>"

def generate_html(vocab_data, examples):
    print("Generating HTML...")
    
    html_content = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>JLPT Vocabulary N5-N1</title>
        <style>
            body { font-family: "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif; background: #f4f4f9; color: #333; margin: 0; padding: 20px; }
            h1 { text-align: center; color: #4a4a4a; }
            .container { max-width: 1000px; margin: 0 auto; background: #fff; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); border-radius: 8px; }
            .level-section { margin-bottom: 40px; }
            .level-header { background: #6c5ce7; color: #fff; padding: 10px 20px; border-radius: 4px; font-size: 1.5em; margin-bottom: 15px; }
            table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
            th, td { border-bottom: 1px solid #eee; padding: 12px; text-align: left; vertical-align: top; }
            th { background: #f8f8f8; font-weight: bold; color: #555; }
            tr:hover { background-color: #fcfcfc; }
            ruby { font-size: 1.2em; }
            rt { font-size: 0.6em; color: #888; }
            .meaning-cn { font-weight: bold; color: #2d3436; }
            .meaning-en { font-size: 0.9em; color: #636e72; margin-top: 4px; }
            .example { margin-top: 6px; font-size: 0.9em; color: #0984e3; background: #f0f8ff; padding: 4px 8px; border-radius: 4px; display: inline-block; }
            .example::before { content: "例: "; font-weight: bold; opacity: 0.7; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>日本語単語帳 N5-N1</h1>
    """
    
    # Group by level
    words_by_level = {"N1": [], "N2": [], "N3": [], "N4": [], "N5": []}
    for entry in vocab_data:
        lvl = entry.get("level", "Uncategorized")
        if lvl in words_by_level:
            words_by_level[lvl].append(entry)
            
    for lvl in ["N5", "N4", "N3", "N2", "N1"]:
        words = words_by_level[lvl]
        if not words: continue
        
        html_content += f'<div class="level-section"><div class="level-header">{lvl} ({len(words)} Words)</div>'
        html_content += '<table><thead><tr><th>Word</th><th>Meaning</th><th>Example</th></tr></thead><tbody>'
        
        for w in words:
            wid = w['id']
            word_ruby = generate_ruby_html(w['word'], w['reading'])
            
            cn = w['meaning_cn']
            en = ", ".join(w['meaning_en'][:2]) if w.get('meaning_en') else ""
            
            ex = examples.get(wid, "No example found.")
            
            html_content += f"""
            <tr>
                <td>{word_ruby}</td>
                <td>
                    <div class="meaning-cn">{cn}</div>
                    <div class="meaning-en">{en}</div>
                </td>
                <td>
                    <div class="example">{ex}</div>
                </td>
            </tr>
            """
        html_content += '</tbody></table></div>'

    html_content += """
        </div>
    </body>
    </html>
    """
    
    with open("vocab_master.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Saved vocab_master.html")

def main():
    # Load Master JSON
    try:
        with open("data_raw/vocab_master.json", "r", encoding="utf-8") as f:
            vocab = json.load(f)
    except FileNotFoundError:
        print("vocab_master.json not found. Run enrichment first.")
        return

    # Load Sentences
    sentences = load_sentences("jpn_sentences.tsv.bz2")
    
    # Match
    examples = match_sentences(vocab, sentences)
    
    # Generate HTML
    generate_html(vocab, examples)

if __name__ == "__main__":
    main()
