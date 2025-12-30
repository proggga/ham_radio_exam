import os
import re
import shutil

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

def clean_content(content):
    # Remove "Related" sections (usually at the end)
    # Match lines starting with optional headers, then "Related", and everything after
    # Using specific patterns seen in the files: "Related:", "## Related", "## Related Notes"
    # We split on the first occurrence of such a line that looks like a section start
    
    # Pattern: Newline, optional whitespace, optional headers (#), optional whitespace, "Related", optional characters, newline
    # This catches:
    # ## Related
    # Related:
    # ## Related Notes
    # Related Links
    content = re.split(r'\n\s*(?:#{1,6}\s*)?Related.*', content, flags=re.IGNORECASE)[0]
    
    # Remove WikiLinks: [[Link|Label]] -> Label, [[Link]] -> Link
    def replace_link(match):
        text = match.group(1)
        if '|' in text:
            return text.split('|')[1]
        return text
    
    content = re.sub(r'\[\[(.*?)\]\]', replace_link, content)
    
    return content.strip()

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
        # Matches: * [[Note]] or * [[Note|Label]] or * **Group**
        # We want to capture the hierarchy if possible, but flat list per section is easier for now.
        
        # Extract links
        matches = re.findall(r'\[\[(.*?)(?:\|.*?)?\]\]', line)
        for note_name in matches:
            structure.append({
                'section': current_section,
                'note': note_name
            })
            
    return structure

def main():
    if not os.path.exists(MASTER_INDEX):
        print("Master Index not found!")
        return

    # Clean docs dir
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)
    os.makedirs(DOCS_DIR)

    index_content = read_file(MASTER_INDEX)
    structure = get_structure(index_content)
    
    # Track file counts per section for numbering
    section_counters = {}
    
    # Buffer for single-file sections
    single_file_buffers = {}

    # Track generated files for README generation: {section: [(filename, title)]}
    section_files = {}

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
        cleaned_body = clean_content(body)
        
        if section in SINGLE_FILE_SECTIONS:
            # Append to buffer
            if section not in single_file_buffers:
                single_file_buffers[section] = []
            single_file_buffers[section].append(f"\n\n{cleaned_body}\n\n---")
        else:
            # Create directory if needed
            section_dir = os.path.join(DOCS_DIR, section)
            if not os.path.exists(section_dir):
                os.makedirs(section_dir)
            
            # Numbering
            count = section_counters.get(section, 0) + 1
            section_counters[section] = count
            
            # Filename: 01_Note_Name.md
            safe_name = note_name.replace(' ', '_').replace('/', '-').replace('(', '').replace(')', '')
            filename = f"{count:02d}_{safe_name}.md"
            
            # Add back link to section README
            cleaned_body += "\n\n---\n[< Back to Section Index](README.md)"

            output_path = os.path.join(section_dir, filename)
            
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

    # Sort sections based on MAPPING order (roughly) - actually structure gives us order but mixed with notes.
    # We can iterate through SECTION_MAPPING to keep order
    
    for header, section_dir in SECTION_MAPPING.items():
        if section_dir in SINGLE_FILE_SECTIONS:
            # It's a file
            main_readme_content.append(f"- [{header}]({section_dir}.md)")
        elif section_dir in section_files:
            # It's a directory
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

if __name__ == "__main__":
    main()
