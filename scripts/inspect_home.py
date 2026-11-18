import re

with open('assets_chunks/Home-i-Cc6tga.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Find all text and titles in Home
strings = re.findall(r'[`"\']([^`"\']{4,300})[`"\']', c)
clean = []
for s in strings:
    if not any(b in s for b in ['stroke-', 'M12', 'viewBox', 'xmlns', 'className', 'http://', 'px', 'calc(', 'flex', 'grid', 'transition']):
        clean.append(s.strip())

seen = set()
for item in clean:
    if item not in seen and len(item) > 10:
        seen.add(item)
        print("-", item)
