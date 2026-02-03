
import json
import os
import time

import google.generativeai as genai

# Set your API key here or via environment variable
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    model = None

def generate_example(word, level, kanji_reading):
    """
    Calls Gemini API to generate an example sentence.
    """
    if not model:
        # Fallback to demo data if no API key
        return {
            "example_sentence": f"これは「{word}」の例文です。",
            "example_reading": f"これは「{word}」のれいぶんです。",
            "example_meaning_cn": f"这是“{word}”的例句。",
            "example_meaning_en": f"This is an example sentence for '{word}'."
        }
    
    prompt = f"""
    Word: {word}
    Reading: {kanji_reading}
    Level: {level}
    
    Provide a natural Japanese example sentence for this word.
    Return ONLY JSON in this format:
    {{
      "example_sentence": "sentence in Japanese",
      "example_reading": "reading of the sentence in Hiragana",
      "example_meaning_cn": "Chinese translation",
      "example_meaning_en": "English translation"
    }}
    """
    
    try:
        response = model.generate_content(prompt)
        # Basic JSON extraction from response
        # Using a simple strip/find since we expect pure JSON
        text = response.text.strip()
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        data = json.loads(text)
        return data
    except Exception as e:
        print(f"Error generating for {word}: {e}")
        return None

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to project root
    project_root = os.path.dirname(script_dir)
    
    data_file = os.path.join(project_root, 'jlpt-web', 'src', 'data', 'vocab.json')
    
    if not os.path.exists(data_file):
        print(f"Error: {data_file} not found.")
        return

    print(f"Reading {data_file}...")
    with open(data_file, 'r', encoding='utf-8') as f:
        vocab_list = json.load(f)

    # Enrich the dataset
    count = 0
    # Increase limit or remove for full run
    limit = int(os.getenv("ENRICH_LIMIT", "50")) 

    for item in vocab_list:
        if count >= limit:
            break
            
        # Skip if already has example (to allow resuming)
        if 'example_sentence' in item and item['example_sentence']:
            continue
            
        print(f"({count+1}/{limit}) Enriching: {item['word']}...")
        enrichment = generate_example(item['word'], item['level'], item.get('kanji_reading', ''))
        
        if enrichment:
            item.update(enrichment)
            count += 1
            # Rate limiting for free tier if needed
            if not os.getenv("GEMINI_API_KEY"):
                pass 
            else:
                time.sleep(1) 

    print(f"Enriched {count} items.")
    
    print(f"Writing back to {data_file}...")
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(vocab_list, f, ensure_ascii=False, indent=2)

    print("Done!")

if __name__ == "__main__":
    main()
