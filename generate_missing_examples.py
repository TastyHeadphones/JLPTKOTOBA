import json
import os
try:
    from openai import OpenAI
except ImportError:
    print("Please install openai: pip install openai")
    OpenAI = None

API_KEY = input("Enter your OpenAI API Key (or press Enter to skip): ").strip()

def generate_examples():
    if not API_KEY or not OpenAI:
        print("Skipping AI generation (No key or module).")
        return

    client = OpenAI(api_key=API_KEY)

    try:
        with open("data_raw/vocab_master_enriched.json", "r", encoding="utf-8") as f:
            vocab = json.load(f)
    except FileNotFoundError:
        print("Run enrichment first.")
        return

    missing_indices = [i for i, w in enumerate(vocab) if w.get('example') == 'No example available.' or w.get('example') == 'No example.']
    
    print(f"Found {len(missing_indices)} words missing examples.")
    
    # Process in batches to save time/requests?
    # Simple loop for now.
    
    for i, idx in enumerate(missing_indices):
        item = vocab[idx]
        word = item['word']
        meaning = item['meaning_cn']
        
        print(f"[{i+1}/{len(missing_indices)}] Generating for: {word} ({meaning})...")
        
        try:
            prompt = f"Make a short, simple Japanese example sentence for the word '{word}' (Meaning: {meaning}). Return ONLY the Japanese sentence."
            
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a Japanese teacher."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=60
            )
            
            sentence = completion.choices[0].message.content.strip()
            vocab[idx]['example'] = sentence
            print(f" -> {sentence}")
            
        except Exception as e:
            print(f"Error: {e}")
            break
            
        # Save every 10
        if i % 10 == 0:
             with open("data_raw/vocab_master_enriched.json", "w", encoding="utf-8") as f:
                json.dump(vocab, f, ensure_ascii=False, indent=2)

    # Final save
    with open("data_raw/vocab_master_enriched.json", "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)
    print("Done.")

if __name__ == "__main__":
    generate_examples()
