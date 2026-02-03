import os
from pypdf import PdfReader

def inspect_pdf(filepath):
    try:
        reader = PdfReader(filepath)
        page = reader.pages[0]
        text = page.extract_text()
        print(f"--- File: {os.path.basename(filepath)} ---")
        print(text[:500])  # Print first 500 chars
        print("\n")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

files = [
    "JN024wordlist.pdf",
    "JN025wordlist.pdf",
    "JN026wordlist.pdf",
    "JN027wordlist.pdf",
    "JN028wordlist.pdf"
]

for f in files:
    inspect_pdf(f)
