import glob
import re
import json
import os

files = sorted(glob.glob('assets_chunks/*.js'))

def extract_strings_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    
    # find template literals and string literals
    raw = re.findall(r'[`"\']([^`"\']{6,800})[`"\']', c)
    filtered = []
    for s in raw:
        # exclude code fragments, css classes, svg paths
        if any(bad in s for bad in ['stroke-', 'M12', 'viewBox', 'xmlns', 'http://www.w3.org', 'style', 'class', 'px', 'calc(', 'flex', 'grid', 'transition', 'duration', 'text-', 'bg-', 'p-', 'm-', 'w-', 'h-', 'rounded', 'border', 'shadow', 'hover:', 'focus:']):
            continue
        # must have letters and spaces
        if ' ' in s and re.search(r'[a-zA-Z]', s):
            filtered.append(s.strip())
    
    # de-duplicate preserving order
    seen = set()
    dedup = []
    for s in filtered:
        if s not in seen:
            seen.add(s)
            dedup.append(s)
    return dedup

site_content = {}
for fp in files:
    name = os.path.basename(fp)
    # Ignore small utility icon files
    if os.path.getsize(fp) < 1000:
        continue
    content = extract_strings_from_file(fp)
    if content:
        site_content[name] = content

with open('full_site_content_summary.json', 'w', encoding='utf-8') as out:
    json.dump(site_content, out, indent=2)

print("Extracted content for", len(site_content), "components/pages.")
for k, v in site_content.items():
    print(f"- {k}: {len(v)} text items")
