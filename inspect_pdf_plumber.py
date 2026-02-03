import pdfplumber
import os

def inspect_pdf_plumber(filepath):
    print(f"--- File: {os.path.basename(filepath)} ---")
    try:
        with pdfplumber.open(filepath) as pdf:
            page = pdf.pages[0]
            # Try to extract tables first
            tables = page.extract_tables()
            if tables:
                print("Tables found:")
                for table in tables[:1]: # Print first table
                    for row in table[:3]: # Print first 3 rows
                        print(row)
            else:
                print("No tables found. Extracting text:")
                print(page.extract_text()[:500])
    except Exception as e:
        print(f"Error: {e}")
    print("\n")

files = [
    "JN024wordlist.pdf", 
    "JN028wordlist.pdf"
]

for f in files:
    inspect_pdf_plumber(f)
