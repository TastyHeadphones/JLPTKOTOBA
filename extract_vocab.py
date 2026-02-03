import pdfplumber
import sys
import json
import re
import os

# Map filenames to JLPT levels
PDF_FILES = {
    "JN024wordlist.pdf": "N1",
    "JN025wordlist.pdf": "N2",
    "JN026wordlist.pdf": "N3",
    "JN027wordlist.pdf": "N4",
    "JN028wordlist.pdf": "N5"
}

def clean_text(text):
    if not text:
        return ""
    return text.strip().replace("\n", " ")

def is_garbage(row):
    """Filter out headers/footers or empty rows"""
    if not row or len(row) < 2:
        return True
    # Check if header row by looking for metadata keywords
    text = "".join([str(x) for x in row if x])
    if "単字表" in text or "作者" in text or "出版" in text or "日本語" in text:
        return True
    return False

def extract_from_pdf(filepath, level):
    words = []
    print(f"Processing {level} from {os.path.basename(filepath)}...")
    
    try:
        with pdfplumber.open(filepath) as pdf:
            for i, page in enumerate(pdf.pages):
                tables = page.extract_tables()
                
                for table in tables:
                    for row in table:
                        if is_garbage(row):
                            continue
                            
                        # Structure varies but usually Col 0 is Word, Col 1 is Meaning (or variations)
                        # Based on inspection: 
                        # N5: ['アイスクリーム', '冰淇淋']
                        # N4: ['あいさつ', '問候，寒暄']
                        # N1: ['さいてん\n祭典', '慶典'] -> Word often contains reading \n kanji or vice versa
                        
                        word_cell = row[0]
                        meaning_cell = row[1] if len(row) > 1 else ""
                        
                        if not word_cell: 
                            continue

                        # Separation logic for cells with newlines (Furigana)
                        # Sometimes it's "reading\nKanji", sometimes "Kanji\nreading"
                        # We will keep raw for now and clean later, or split distinct lines
                        
                        entry = {
                            "raw_word": str(word_cell),
                            "meaning_cn": clean_text(str(meaning_cell)),
                            "level": level
                        }
                        words.append(entry)
                        
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        
    print(f"  Extracted {len(words)} entries.")
    return words

def main():
    all_words = []
    
    # Ensure raw output dir
    os.makedirs("data_raw", exist_ok=True)

    for filename, level in PDF_FILES.items():
        if os.path.exists(filename):
            data = extract_from_pdf(filename, level)
            all_words.extend(data)
        else:
            print(f"Warning: File {filename} not found.")

    output_file = "data_raw/words_raw.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_words, f, ensure_ascii=False, indent=2)
    
    print(f"\nTotal extracted: {len(all_words)}")
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    main()
