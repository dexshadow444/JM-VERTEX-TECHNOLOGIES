import re
import json

with open('index.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

print('JS file size:', len(content))

# Extract all string literals or routes
paths = re.findall(r'["\'](/[\w\-/]*)["\']', content)
clean_paths = sorted(list(set([p for p in paths if len(p) > 1 and not p.endswith(('.png', '.svg', '.jpg', '.css', '.js'))])))
print('Potential Paths:', clean_paths)

# Find sections, headings, titles
titles = re.findall(r'title:\s*["\']([^"\']+)["\']', content)
print('Titles:', titles[:15])

# Find services or items
services = re.findall(r'name:\s*["\']([^"\']+)["\']', content)
print('Names:', services[:20])
