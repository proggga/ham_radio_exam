import os
import re
import shutil
from urllib.parse import unquote

ZETTEL_DIR = "zettelkasten"
DOCS_DIR = "docs"
MASTER_INDEX = os.path.join(ZETTEL_DIR, "Master Index.md")

# Mapping from Master Index headers to output directories/files
SECTION_MAPPING = {
    "0. Basic Skills": "00_basic_skills",
    "1. Electricity & Theory": "01_electricity",
    "2. Components": "02_components",
    "3. Circuits": "03_circuits",
    "4. Receivers": "04_receivers",
    "5. Transmitters": "05_transmitters",
    "6. Antennas": "06_antennas",
    "7. Propagation": "07_propagation",
    "8. Measurements": "08_measurements",
    "9. Interference (EMC)": "09_interference",
    "10. Safety": "10_safety",
    "11. Procedures": "11_procedures",
    "12. Regulations": "12_regulations",
    "13. Conduct": "13_conduct"
}

# Sections that should be single files instead of directories (based on user preference)
SINGLE_FILE_SECTIONS = {
    "00_basic_skills",
    "11_procedures",
    "13_conduct"
}

# Notes to exclude
EXCLUDE_NOTES = {
    "README",
    "Master Index"
}

def read_file(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def strip_frontmatter(content):
    if content.startswith('---'):
        try:
            _, frontmatter, body = content.split('---', 2)
            return body.strip()
        except ValueError:
            return content
    return content

def get_structure(index_content):
    lines = index_content.split('\n')
    structure = [] 
    current_section = None
    
    for line in lines:
        line = line.strip()
        # Check for Headers (## X. Section)
        header_match = re.match(r'^##\s+(.*)', line)
        if header_match:
            header_text = header_match.group(1).strip()
            # Find matching directory
            for key, val in SECTION_MAPPING.items():
                if key in header_text:
                    current_section = val
                    break
            else:
                # If no match found, maybe use a misc folder or skip
                current_section = None
            continue
            
        if not current_section:
            continue
            
        # Find links
        matches = re.findall(r'\[\[(.*?)(?:\|.*?)?\]\]', line)
        for note_name in matches:
            structure.append({
                'section': current_section,
                'note': note_name
            })
            
    return structure

def get_linked_notes(content):
    # Extract all [[WikiLinks]] from content
    # return list of note names
    matches = re.findall(r'\[\[(.*?)(?:\|.*?)?\]\]', content)
    return matches

def is_index_note(content):
    # Check frontmatter for type: index or type: map
    if content.startswith('---'):
        try:
            _, frontmatter, _ = content.split('---', 2)
            if re.search(r'type:\s*(?:index|map)', frontmatter, re.IGNORECASE):
                return True
            if re.search(r'tags:.*(?:index|map)', frontmatter, re.IGNORECASE | re.DOTALL):
                return True
        except ValueError:
            pass
    return False

def expand_structure(structure):
    # Map canonical sections for notes explicitly in the Master Index
    canonical_map = {item['note']: item['section'] for item in structure}
    
    # Expand index notes recursively
    
    def process_note(note_name, section, depth=0):
        if depth > 5: return [] # Safety break
        
        # If this is a child node (depth > 0) and it has a canonical home elsewhere,
        # do NOT add it here. It will be added when its canonical section is processed.
        if depth > 0:
            canonical = canonical_map.get(note_name)
            if canonical and canonical != section:
                return []

        items = []
        
        items.append({'section': section, 'note': note_name})
        
        # Read file to check if index
        note_path = os.path.join(ZETTEL_DIR, note_name + ".md")
        content = read_file(note_path)
        if not content: return items
        
        if is_index_note(content):
            # Extract children
            # We want to exclude "Related" section links usually
            body = strip_frontmatter(content)
            body_main = re.split(r'\n\s*(?:#{1,6}\s*)?Related.*', body, flags=re.IGNORECASE)[0]
            
            children = get_linked_notes(body_main)
            for child in children:
                # Recursively process
                items.extend(process_note(child, section, depth+1))
                
        return items

    # Build full list including duplicates
    full_list = []
    for item in structure:
        expanded = process_note(item['note'], item['section'])
        full_list.extend(expanded)

    # Filter duplicates, keeping FIRST occurrence
    final_structure = []
    final_seen = set()
    
    for item in full_list:
        if item['note'] not in final_seen and item['note'] not in EXCLUDE_NOTES:
            final_structure.append(item)
            final_seen.add(item['note'])
            
    return final_structure

def main():
    if not os.path.exists(MASTER_INDEX):
        print("Master Index not found!")
        return

    # Clean docs dir
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)
    os.makedirs(DOCS_DIR)

    index_content = read_file(MASTER_INDEX)
    initial_structure = get_structure(index_content)
    
    # Expand structure to include children of Index/Map notes
    structure = expand_structure(initial_structure)
    
    print(f"Structure expanded from {len(initial_structure)} to {len(structure)} notes.")
    
    # --- Pass 1: Calculate destination paths for all notes ---
    # map: note_name -> (section_dir, filename)
    note_destinations = {} 
    
    section_counters = {}
    
    for item in structure:
        section = item['section']
        note_name = item['note']
        
        if note_name in EXCLUDE_NOTES:
            continue
            
        if section in SINGLE_FILE_SECTIONS:
            # Single files live in the root of DOCS_DIR
            # We treat the filename as the section name .md
            filename = f"{section}.md"
            note_destinations[note_name] = ("", filename) # Root dir, filename
        else:
            # Numbering
            count = section_counters.get(section, 0) + 1
            section_counters[section] = count
            
            # Filename: 01_Note_Name.md
            safe_name = note_name.replace(' ', '_').replace('/', '-').replace('(', '').replace(')', '')
            filename = f"{count:02d}_{safe_name}.md"
            note_destinations[note_name] = (section, filename)

    # --- Pass 2: Generate Content and Resolve Links ---
    
    # Helper to resolve links
    def resolve_links(content, current_section_dir):
        def replace_link(match):
            full_link = match.group(1)
            if '|' in full_link:
                target_note, label = full_link.split('|', 1)
            else:
                target_note, label = full_link, full_link
            
            # Find target
            if target_note in note_destinations:
                target_section, target_file = note_destinations[target_note]
                
                # Construct relative path
                if current_section_dir == "": # We are in root (Single file section)
                    if target_section == "":
                        path = target_file
                    else:
                        path = f"{target_section}/{target_file}"
                else: # We are in a subdirectory
                    if target_section == "":
                        path = f"../{target_file}"
                    elif target_section == current_section_dir:
                        path = target_file
                    else:
                        path = f"../{target_section}/{target_file}"
                        
                return f"[{label}]({path})"
            else:
                # Log missing targets (excluding self-links or intentional stubs if any)
                print(f"Warning: Link target '{target_note}' not found in destinations (referenced in {note_name})")
                return label

        return re.sub(r'\[\[(.*?)\]\]', replace_link, content)

    # Helper for cleaning content (modified to accept resolver)
    def clean_and_link_content(content, current_section_dir):
        # Remove "Related" sections first
        content = re.split(r'\n\s*(?:#{1,6}\s*)?Related.*', content, flags=re.IGNORECASE)[0]
        # Resolve links
        content = resolve_links(content, current_section_dir)
        return content.strip()

    # Track files for README generation
    section_files = {} # {section: [(filename, note_name)]}
    single_file_buffers = {} # {section: [content]}

    # Reset counters for actual generation iteration (though we use destinations now)
    # Actually we can iterate structure again
    
    for item in structure:
        section = item['section']
        note_name = item['note']
        
        if note_name in EXCLUDE_NOTES:
            continue
            
        note_path = os.path.join(ZETTEL_DIR, note_name + ".md")
        raw_content = read_file(note_path)
        
        if not raw_content:
            print(f"Warning: Note not found: {note_name}")
            continue
            
        body = strip_frontmatter(raw_content)
        
        if section in SINGLE_FILE_SECTIONS:
            # We are generating a single file at root
            # Current dir is root ("")
            cleaned_body = clean_and_link_content(body, "")
            
            if section not in single_file_buffers:
                single_file_buffers[section] = []
            
            # Add a header for the note within the single file to separate them
            single_file_buffers[section].append(f"\n\n{cleaned_body}\n\n---")
            
        else:
            dest = note_destinations.get(note_name)
            if not dest: continue
            
            target_section, filename = dest
            
            # Create directory if needed
            section_dir_path = os.path.join(DOCS_DIR, target_section)
            if not os.path.exists(section_dir_path):
                os.makedirs(section_dir_path)
            
            # We are generating a file inside target_section
            cleaned_body = clean_and_link_content(body, target_section)
            
            # Add back link
            cleaned_body += "\n\n---\n[< Back to Section Index](README.md)"

            output_path = os.path.join(section_dir_path, filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_body)
            
            # Track for README
            if section not in section_files:
                section_files[section] = []
            section_files[section].append((filename, note_name))

    # Write single file sections
    for section, content_list in single_file_buffers.items():
        output_path = os.path.join(DOCS_DIR, section + ".md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# {section.replace('_', ' ').title()}\n")
            f.write(f"\n[< Back to Main Index](README.md)\n")
            f.write("\n".join(content_list))

    # Generate Main README and Section READMEs
    main_readme_content = ["# Ham Radio Exam Study Guide\n\n## Table of Contents\n"]

    for header, section_dir in SECTION_MAPPING.items():
        if section_dir in SINGLE_FILE_SECTIONS:
            main_readme_content.append(f"- [{header}]({section_dir}.md)")
        elif section_dir in section_files:
            main_readme_content.append(f"- [{header}]({section_dir}/README.md)")
            
            # Generate Section README
            section_readme_path = os.path.join(DOCS_DIR, section_dir, "README.md")
            with open(section_readme_path, 'w', encoding='utf-8') as f:
                f.write(f"# {header}\n\n")
                f.write("[< Back to Main Index](../README.md)\n\n")
                for fname, note_title in section_files[section_dir]:
                    f.write(f"- [{note_title}]({fname})\n")

    with open(os.path.join(DOCS_DIR, "README.md"), 'w', encoding='utf-8') as f:
        f.write("\n".join(main_readme_content))

    print(f"Successfully regenerated docs in {DOCS_DIR}")
    
    update_main_readme(note_destinations)

def update_main_readme(note_destinations):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("Main README.md not found, skipping link update.")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_link(match):
        text = match.group(1)
        url = match.group(2)

        # Check if it's a zettelkasten link
        if not url.startswith("zettelkasten/"):
            return match.group(0)

        # Extract note filename
        basename = url.split('/')[-1]
        note_name_encoded = os.path.splitext(basename)[0]
        note_name = unquote(note_name_encoded).strip()

        # Look up in destinations
        if note_name in note_destinations:
            section, filename = note_destinations[note_name]
            if section:
                new_path = f"docs/{section}/{filename}"
            else:
                new_path = f"docs/{filename}"
            return f"[{text}]({new_path})"
        else:
            return match.group(0)

    new_content = re.sub(r'\[([^\]]+)\]\((zettelkasten/.*?\.md)\)', replace_link, content)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Updated links in main README.md")

if __name__ == "__main__":
    main()
