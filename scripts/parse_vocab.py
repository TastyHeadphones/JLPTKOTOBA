
import re
import json
import os

def parse_markdown_table(markdown_content):
    """
    Parses markdown tables from the provided content.
    Returns a dictionary structured by N-level.
    """
    lines = markdown_content.split('\n')
    data = {}
    current_level = None
    
    # Regex to identify headers like "## N5 (699 Words)"
    level_header_regex = re.compile(r'^##\s+(N\d+)')
    # Regex to identify table rows
    table_row_regex = re.compile(r'^\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|$')

    for line in lines:
        line = line.strip()
        
        # Check for Level Header
        level_match = level_header_regex.match(line)
        if level_match:
            current_level = level_match.group(1)
            data[current_level] = []
            print(f"Found Level: {current_level}")
            continue

        # Skip separator lines like |---|---|---|
        if '---' in line:
            continue

        # Check for Table Row
        # Expecting columns: Word | Reading | Meaning (CN) | Meaning (EN)
        row_match = table_row_regex.match(line)
        if row_match and current_level:
            word = row_match.group(1).strip()
            # Headers row check
            if word == 'Word':
                continue
                
            reading = row_match.group(2).strip()
            meaning_cn = row_match.group(3).strip()
            meaning_en = row_match.group(4).strip()
            
            # Simple unique ID generation (can be improved)
            unique_id = f"{current_level}_{len(data[current_level])}"

            item = {
                "id": unique_id,
                "word": word,
                "reading": reading,
                "meaning_cn": meaning_cn,
                "meaning_en": meaning_en,
                "level": current_level
            }
            data[current_level].append(item)

    return data

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to project root
    project_root = os.path.dirname(script_dir)
    
    source_file = os.path.join(project_root, 'vocab_master.md')
    output_file = os.path.join(project_root, 'jlpt-web', 'src', 'data', 'vocab.json')
    
    # Ensure source exists
    if not os.path.exists(source_file):
        print(f"Error: {source_file} not found.")
        return

    print(f"Reading {source_file}...")
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Parsing content...")
    parsed_data = parse_markdown_table(content)
    
    # Flatten data for easier consumption in React if needed, 
    # but keeping it by level is also fine. Let's return a flat list for now with a 'level' property.
    flat_list = []
    for level, items in parsed_data.items():
        print(f"Level {level}: {len(items)} words")
        flat_list.extend(items)

    # Ensure output directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Writing parsed data to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(flat_list, f, ensure_ascii=False, indent=2)

    print("Done!")

if __name__ == "__main__":
    main()
