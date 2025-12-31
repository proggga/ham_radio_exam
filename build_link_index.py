import os
import re
import json

ZETTELKASTEN_DIR = "/Users/mfesenko/ham_radio_exam/zettelkasten"
OUTPUT_FILE = os.path.join(ZETTELKASTEN_DIR, "link_index.json")

def extract_title(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        match = re.search(r'^title:\s*"?([^"\n]+)"?', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return None

def generate_keywords(title, filename):
    keywords = set()
    
    # 1. Full Title
    keywords.add(title)
    
    # 2. Filename without extension (often same as title, but good to have)
    keywords.add(filename.replace('.md', ''))
    
    # 3. Parentheses: "Standing Wave Ratio (SWR)" -> "SWR", "Standing Wave Ratio"
    paren_match = re.search(r'^(.*)\s*\(([^)]+)\)$', title)
    if paren_match:
        main_part = paren_match.group(1).strip()
        paren_part = paren_match.group(2).strip()
        keywords.add(main_part)
        keywords.add(paren_part)
    
    # 4. Ampersands: "Analogue Modulation & AM" -> "Analogue Modulation", "AM"
    if " & " in title:
        parts = title.split(" & ")
        for part in parts:
            keywords.add(part.strip())

    # 5. Clean up
    clean_keywords = set()
    for k in keywords:
        k = k.strip()
        if len(k) < 2: 
            continue
        # Avoid very common short words if they end up as keywords
        if k.lower() in ["the", "a", "an", "and", "or", "of", "to", "in", "on", "at", "by", "for", "with", "vs", "map"]:
            continue
        clean_keywords.add(k)
        
    return list(clean_keywords)

def build_index():
    index = {}
    if not os.path.exists(ZETTELKASTEN_DIR):
        print(f"Directory not found: {ZETTELKASTEN_DIR}")
        return {}

    files = [f for f in os.listdir(ZETTELKASTEN_DIR) if f.endswith('.md') and f != "Master Index.md"]
    
    temp_index = []
    
    for filename in files:
        filepath = os.path.join(ZETTELKASTEN_DIR, filename)
        title = extract_title(filepath)
        if not title:
            title = filename.replace('.md', '')
            
        keywords = generate_keywords(title, filename)
        target_file = filename.replace('.md', '')
        
        for kw in keywords:
            temp_index.append((kw, target_file))
            
    # Sort by length of keyword descending to ensure we match longest phrases first
    temp_index.sort(key=lambda x: len(x[0]), reverse=True)
    
    index_dict = {}
    for kw, target in temp_index:
        if kw not in index_dict:
             index_dict[kw] = target
             
    return index_dict

if __name__ == "__main__":
    index = build_index()
    
    manual_additions = {
        "D-STAR": "Modern Digital Modes",
        "DMR": "Modern Digital Modes",
        "FT8": "Modern Digital Modes",
        "Yagi": "Directional Antennas (Beams)",
        "Dipole": "The Dipole Antenna",
        "Resistor": "Resistors",
        "Capacitor": "Capacitors",
        "Inductor": "Inductors (Spoelen)",
        "Diode": "Diodes",
        "Transistor": "Transistors (BJT & FET)",
        "Op-Amps": "Operational Amplifiers (Op-Amps)",
        "OpAmp": "Operational Amplifiers (Op-Amps)",
        "NVIS": "Near Vertical Incidence Skywave (NVIS)",
        "UHF": "VHFUHF Bands (6m, 2m, 70cm)",
        "VHF": "VHFUHF Bands (6m, 2m, 70cm)",
        "HF": "Propagation Basics",
        "ATU": "Antenna Tuning Unit (ATU)",
        "SWR": "Standing Wave Ratio (SWR)",
        "SSB": "Single Sideband (SSB)",
        "FM": "Frequency Modulation (FM)",
        "AM": "Analogue Modulation & AM",
        "CW": "CW Abbreviations & Prosigns",
        "Ohm's Law": "Voltage, Current, and Ohm's Law",
        "Q-factor": "Quality Factor (Q)",
        "Skin Effect": "Skin Effect",
        "RIT": "Common Transceiver Controls",
        "Clarifier": "Common Transceiver Controls",
        "Squelch": "Common Transceiver Controls",
        "AGC": "Automatic Gain Control (AGC)",
        "PEP": "Analogue Modulation & AM",
        "Decibels": "Decibels & Logarithms",
        "dB": "Decibels & Logarithms",
        "Safety": "Electrical Safety",
        "Mixer": "Mixers",
        "Rectifier": "Rectification",
        "Semiconductor": "Semiconductors",
        "Filter": "Filters & Resonance",
        "Logic Gate": "Digital Logic Gates",
        "Ionosphere": "The Ionosphere",
    }
    
    for kw, target in manual_additions.items():
        index[kw] = target
            
    with open(OUTPUT_FILE, "w") as f:
        json.dump(index, f, indent=4)
    
    print(f"Index built with {len(index)} keywords. Saved to {OUTPUT_FILE}")
