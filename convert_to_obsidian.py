import os
import re
import glob

SOURCE_DIR = "/Users/mfesenko/ham_radio_exam/zettelkasten"
ROOT_README = "/Users/mfesenko/ham_radio_exam/README.md"

def get_frontmatter_value(content, key):
    # Simple regex to find "key: value" in the first YAML block
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    fm_text = match.group(1)
    
    # Look for key: value
    # Handle simple strings, maybe quotes
    key_match = re.search(r'^' + re.escape(key) + r':\s*(.*)$', fm_text, re.MULTILINE)
    if key_match:
        val = key_match.group(1).strip()
        # Remove quotes if present
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        return val
    return None

def clean_filename(title):
    # Remove invalid chars and common confusion chars
    clean = re.sub(r'[<>:"/\|?*]', '', title)
    # Remove "Map: " prefix if present, it's redundant in filename if we want clean names
    clean = clean.replace("Map: ", "")
    clean = clean.strip()
    return f"{clean}.md"

def main():
    files = glob.glob(os.path.join(SOURCE_DIR, "*.md"))
    mapping = {} # old_basename_no_ext -> new_basename_no_ext
    file_info = [] # list of dicts

    print(f"Phase 1: Analyzing {len(files)} files...")
    
    # First pass: Determine new names and build mapping
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        title = get_frontmatter_value(content, 'title')
        file_id = get_frontmatter_value(content, 'id')
        
        old_basename = os.path.basename(file_path)
        old_name_no_ext = os.path.splitext(old_basename)[0]
        
        if title:
            new_filename = clean_filename(title)
        else:
            # Fallback to cleanup existing filename if no title
            # e.g. 20230101-slug -> Slug.md
            parts = old_name_no_ext.split('-', 1)
            if len(parts) > 1 and parts[0].isdigit() and len(parts[0]) >= 12:
                slug = parts[1].replace('-', ' ').title()
                new_filename = f"{slug}.md"
            else:
                new_filename = old_basename

        # Check for collisions in file_info
        existing_names = [x['new_filename'] for x in file_info]
        if new_filename in existing_names:
            print(f"Warning: Collision for {new_filename}. Appending ID.")
            if file_id:
                new_filename = new_filename.replace(".md", f" {file_id}.md")
            else:
                # Append random digits or counter? 
                new_filename = new_filename.replace(".md", "_1.md")

        file_info.append({
            'old_path': file_path,
            'old_name_no_ext': old_name_no_ext,
            'new_filename': new_filename,
            'new_name_no_ext': os.path.splitext(new_filename)[0],
            'content': content
        })
        
        mapping[old_name_no_ext] = os.path.splitext(new_filename)[0]

    print(f"Mapped {len(mapping)} files.")

    print("Phase 2: Updating content and renaming...")
    for info in file_info:
        content = info['content']
        
        # 1. Update Wiki Links [[20230101-old-name]] -> [[New Name]]
        # Also handles [[20230101-old-name|Alias]] -> [[New Name|Alias]]
        def replace_wiki(match):
            target = match.group(1)
            alias = match.group(2) if match.group(2) else "" # includes |
            
            # Handle anchor links [[note#heading]]
            anchor = ""
            if '#' in target:
                base, anchor_part = target.split('#', 1)
                target = base
                anchor = '#' + anchor_part

            if target in mapping:
                new_target = mapping[target]
                return f"[[{new_target}{anchor}{alias}]]"
            
            return match.group(0)

        content = re.sub(r'\[\[(.*?)(?:(\|.*?))?\]\]', replace_wiki, content)
        
        # 2. Update Standard Markdown Links [Text](20230101-old-name.md) -> [[New Name|Text]]
        # User requested rich use of WikiLinks.
        def replace_md(match):
            text = match.group(1)
            link = match.group(2)
            
            # We care about relative links to .md files
            if link.endswith('.md') and not link.startswith('http'):
                # Extract basename just in case path is used
                base_link = os.path.basename(link)[:-3]
                if base_link in mapping:
                    new_target = mapping[base_link]
                    # Convert to WikiLink [[New Name|Text]]
                    # If text is same as new name, just [[New Name]]
                    if text == new_target:
                        return f"[[{new_target}]]"
                    return f"[[{new_target}|{text}]]"
            
            return match.group(0)

        content = re.sub(r'\[(.*?)\]\((.*?)\)', replace_md, content)

        # Write content
        new_path = os.path.join(SOURCE_DIR, info['new_filename'])
        
        # Only rewrite if content changed or name changed
        # Actually always rewrite to be safe
        with open(info['old_path'], 'w', encoding='utf-8') as f:
            f.write(content)
            
        if info['old_path'] != new_path:
            os.rename(info['old_path'], new_path)
            print(f"Renamed: {os.path.basename(info['old_path'])} -> {info['new_filename']}")

    # Phase 3: Update ROOT README
    if os.path.exists(ROOT_README):
        print("Phase 3: Updating root README.md...")
        with open(ROOT_README, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def replace_readme_link(match):
            text = match.group(1)
            link = match.group(2)
            
            if "zettelkasten/" in link and link.endswith(".md"):
                basename = os.path.basename(link)[:-3]
                if basename in mapping:
                    new_name = mapping[basename]
                    # Keep markdown format for external compatibility, but point to new file
                    # Ensure spaces are handled if needed, though most md viewers handle spaces fine 
                    # or require %20. We'll stick to literal spaces as usually preferred by Obsidian users
                    # but since this is the root README, maybe %20 is safer? 
                    # Let's use simple path.
                    return f"[{text}](zettelkasten/{new_name}.md)"
            return match.group(0)

        content = re.sub(r'\[(.*?)\]\((.*?)\)', replace_readme_link, content)
        
        with open(ROOT_README, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("Migration complete.")

if __name__ == "__main__":
    main()
