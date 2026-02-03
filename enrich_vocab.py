import json
import re
import os
from jamdict import Jamdict

def clean_word_entry(raw_word):
    """
    Parses 'reading\\nWord' or 'Word' into (Word, Reading).
    Removes internal spaces from Word which are often PDF artifacts.
    """
    parts = raw_word.split('\n')
    
    if len(parts) >= 2:
        # Assuming format is Reading \n Kanji like "さいてん\n祭典"
        reading = parts[0].strip().replace(" ", "")
        word = parts[1].strip().replace(" ", "")
        return word, reading
    else:
        # Just one line, e.g. "ミュンヘン"
        word = parts[0].strip().replace(" ", "")
        return word, "" # No separate reading available/needed

def extract_primary_english_meanings(entry):
    """Extracts first few English meanings from JMDict entry."""
    meanings = []
    for sense in entry.senses:
        meanings.extend([g.text for g in sense.gloss])
    return meanings[:3] # Return top 3 meanings

def enrich_words():
    print("Loading Jamdict (this may take a moment)...")
    jmd = Jamdict()
    
    with open("data_raw/words_raw.json", "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    
    enriched_data = []
    
    print(f"Enriching {len(raw_data)} words...")
    
    count = 0
    for item in raw_data:
        word, reading = clean_word_entry(item["raw_word"])
        
        entry = {
            "id": count,
            "word": word,
            "reading": reading, # From PDF if available
            "meaning_cn": item["meaning_cn"],
            "level": item["level"],
            "meaning_en": [],
            "examples": []
        }

        # Lookup in JMDict
        # Strategies:
        # 1. Exact match on word
        # 2. If reading provided, match on word + reading
        
        try:
            lookup_res = jmd.lookup(word)
        except Exception as e:
            print(f"Error looking up {word}: {e}")
            lookup_res = None
        
        if lookup_res and lookup_res.entries:
            # Take the first matching entry
            # In a real app we might want to be smarter about selecting the right entry based on reading
            target_entry = lookup_res.entries[0]
            
            # If we have a reading, try to find an entry that matches both word and reading
            if reading:
                for e in lookup_res.entries:
                     # Check if reading is in kana forms of the entry
                     kana_forms = [k.text for k in e.kana_forms]
                     if reading in kana_forms:
                         target_entry = e
                         break
            
            entry["meaning_en"] = extract_primary_english_meanings(target_entry)
            
            # Get examples from Tatoeba via jamdict
            # Note: jamdict.lookup returns characters which we can use to find sentences
            # Wait, jmd.lookup doesn't return sentences directly usually unless configured?
            # Standard jamdict allows looking up distinct sentences. 
            # We can use jmd.lookup(query) which searches everything, but here we want sentences specifically.
            # Let's try searching specifically for sentences if possible or rely on the lookup result if it includes them.
            # looking at Jamdict implementation, standard lookup usually queries dict.
            # We will use jmd.import_data() if necessary but usually it comes pre-packaged?
            # Actually, let's try a sentence search if the library supports it easily, otherwise skip to keep it fast.
            # Jamdict usually requires a separate sentence DB. Assuming standard pypi install has it or we might skip it if empty.
            
            # Let's try to just get meanings first to be safe. "examples" might be empty if no DB.
            pass

        enriched_data.append(entry)
        count += 1
        
        if count % 100 == 0:
            print(f"Processed {count} words...")


    # Save Master Data
    with open("data_raw/vocab_master.json", "w", encoding="utf-8") as f:
        json.dump(enriched_data, f, ensure_ascii=False, indent=2)
    
    # Generate Markdown
    md_content = "# 日本語語彙 N5-N1\n\n"
    
    # Group by level
    words_by_level = {"N1": [], "N2": [], "N3": [], "N4": [], "N5": []}
    for entry in enriched_data:
        lvl = entry.get("level", "Uncategorized")
        if lvl in words_by_level:
            words_by_level[lvl].append(entry)
    
    for lvl in ["N5", "N4", "N3", "N2", "N1"]:
        words = words_by_level[lvl]
        md_content += f"## {lvl} ({len(words)} Words)\n\n"
        md_content += "| Word | Reading | Meaning (CN) | Meaning (EN) |\n"
        md_content += "|---|---|---|---|\n"
        for w in words:
            # Format: Word (Reading if exists)
            term = w['word']
            if w['reading']:
                term += f" ({w['reading']})"
            
            en_meanings = ", ".join(w['meaning_en'][:2]) if w['meaning_en'] else "-"
            md_content += f"| {term} | {w['reading']} | {w['meaning_cn']} | {en_meanings} |\n"
        md_content += "\n"

    with open("vocab_master.md", "w", encoding="utf-8") as f:
        f.write(md_content)

    print("Done enrichment and Markdown generation.")

if __name__ == "__main__":
    enrich_words()
