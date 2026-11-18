import os
import glob
import re
import json

files = glob.glob('assets_chunks/*.js')

parsed_data = {}

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        code = f.read()
    
    # Extract strings
    strings = re.findall(r'["\']([^"\']{5,400})["\']', code)
    # Filter code noise
    clean_strings = []
    for s in strings:
        if any(bad in s for bad in ['stroke-', 'M12', 'viewBox', 'xmlns', 'http://www.w3.org', 'useMemo', 'useState', 'useEffect']):
            continue
        clean_strings.append(s)
    
    parsed_data[fname] = clean_strings

with open('full_chunk_text.json', 'w', encoding='utf-8') as out:
    json.dump(parsed_data, out, indent=2)

print("Saved full text extraction to full_chunk_text.json")
