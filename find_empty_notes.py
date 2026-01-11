import os
import re

ZETTEL_DIR = "zettelkasten"
MASTER_INDEX = "Master Index.md"

def get_all_notes():
    if not os.path.exists(ZETTEL_DIR):
        return []
    return [f for f in os.listdir(ZETTEL_DIR) if f.endswith(".md")]

def analyze_notes(notes):
    ghost_links = set()
    low_content_notes = []
    
    # Set of valid note names (without extension) for quick lookup
    valid_note_names = {n.replace(".md", "") for n in notes}
    
    for filename in notes:
        filepath = os.path.join(ZETTEL_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check for low content
            # Strip frontmatter
            body = content
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    body = parts[2]
            
            # Strip whitespace
            clean_body = body.strip()
            
            # Criteria: Less than 100 characters of real text
            if len(clean_body) < 50:
                 low_content_notes.append((filename, len(clean_body)))

            # Check for ghost links
            # Matches [[Link]] or [[Link|Alias]]
            matches = re.findall(r'\[\[(.*?)(?:\|.*?)?\]\]', content)
            for link in matches:
                link_clean = link.strip()
                if link_clean not in valid_note_names:
                    ghost_links.add(link_clean)
                    
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    return ghost_links, low_content_notes

def main():
    notes = get_all_notes()
    if not notes:
        print("No notes found.")
        return

    ghosts, empties = analyze_notes(notes)
    
    print(f"--- Ghost Notes (Linked but don't exist) ---")
    if ghosts:
        for g in sorted(ghosts):
            print(f"- [[{g}]]")
    else:
        print("None")
        
    print(f"\n--- Low Content Notes (< 50 chars body) ---")
    if empties:
        for note, size in sorted(empties):
            print(f"- {note} (Body length: {size})")
    else:
        print("None")

if __name__ == "__main__":
    main()
