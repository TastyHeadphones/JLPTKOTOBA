import json
from add_examples_and_html import match_sentences, load_sentences

def check_missing():
    try:
        with open("data_raw/vocab_master.json", "r", encoding="utf-8") as f:
            vocab = json.load(f)
    except:
        print("No master json")
        return

    # Check matches again (fast check)
    # Actually we don't need to re-scan if we trust the previous run, 
    # but we didn't save the matched examples to a file, just generated HTML.
    # We should have saved them. 
    # Let's verify coverage by just loading valid sentences and checking a small set?
    # No, to answer "how many missing", we need to run the match.
    
    print(f"Total words: {len(vocab)}")
    
    # Let's do a quick estimate or just run the matcher if it's fast enough.
    # The matcher took ~30s before.
    
    sentences = load_sentences("jpn_sentences.tsv.bz2")
    examples = match_sentences(vocab, sentences)
    
    missing_count = 0
    missing_words = []
    
    for item in vocab:
        if item['id'] not in examples:
            missing_count += 1
            missing_words.append(item['word'])
            
    print(f"\nMissing Examples: {missing_count}/{len(vocab)}")
    print("First 10 missing:", missing_words[:10])
    
    # Save missing for review
    with open("missing_examples.json", "w") as f:
        json.dump(missing_words, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    check_missing()
