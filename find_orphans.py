import os
import re
from collections import defaultdict

ZETTEL_DIR = "zettelkasten"
MASTER_INDEX = "Master Index.md"

def get_all_notes():
    notes = []
    if not os.path.exists(ZETTEL_DIR):
        print(f"Directory {ZETTEL_DIR} not found.")
        return []
    
    for filename in os.listdir(ZETTEL_DIR):
        if filename.endswith(".md"):
            # Normalize matches
            notes.append(filename)
    return notes

def find_links_in_file(filepath):
    links = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Match [[Link]] or [[Link|Alias]]
            matches = re.findall(r'\[\[(.*?)(?:\|.*?)?\]\]', content)
            for match in matches:
                # The link target is the filename without extension (usually)
                link_target = match.strip()
                if not link_target.lower().endswith(".md"):
                    link_target += ".md"
                links.add(link_target)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return links

def main():
    all_notes = get_all_notes()
    if not all_notes:
        print("No notes found.")
        return

    # Dictionary to track incoming links: note_filename -> set of source_filenames
    incoming_links = defaultdict(set)

    # Populate incoming links
    for source_note in all_notes:
        source_path = os.path.join(ZETTEL_DIR, source_note)
        links = find_links_in_file(source_path)
        
        for target in links:
            # Check if target exists in our notes list
            if target in all_notes:
                incoming_links[target].add(source_note)

    orphans = []
    for note in all_notes:
        # Master Index is the root, it doesn't need incoming links
        if note == MASTER_INDEX:
            continue
        
        if note not in incoming_links:
            orphans.append(note)

    if orphans:
        print(f"Found {len(orphans)} orphan notes (not linked from any file):")
        for orphan in sorted(orphans):
            print(f"- {orphan}")
    else:
        print("No orphan notes found. All notes are linked!")

if __name__ == "__main__":
    main()
