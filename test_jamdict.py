from jamdict import Jamdict

def test_examples():
    jmd = Jamdict()
    word = "祭典"
    print(f"Searching examples for {word}...")
    
    # Try different search methods to find sentences
    # Jamdict usually pairs with a sentence DB if available.
    result = jmd.lookup(word)
    
    # Check if chars or entries give us links to sentences? 
    # Usually we need to query explicitly for sentences using .search() logic if not exposed in lookup
    
    # Let's try searching for sentences directly if possible.
    # Based on Jamdict source, it uses 'minidict.db' or similar. 
    # Let's see if we can access the 'sentences' via the search context or helper.
    
    # In Jamdict 0.1a+:
    # jmd.lookup(query) returns a result object.
    
    print("Entries:", len(result.entries))
    if result.entries:
        print("First Entry:", result.entries[0])
        
    print("Chars:", len(result.chars))
    
    # Try raw search on 'sentence' table if standard lookup fails
    # jmd.jmdict.db is the sqlite connection usually?
    # Or jmd.krad is for kanji components.
    
    # Let's inspect the `Jamdict` object capabilities
    print("Dir(jmd):", dir(jmd))

if __name__ == "__main__":
    test_examples()
