import re

with open('assets_chunks/Home-i-Cc6tga.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Search for whatsappNum
matches = re.finditer(r'whatsappNum', c)
for m in matches:
    start = max(0, m.start() - 250)
    end = min(len(c), m.end() + 250)
    print(c[start:end])
    print("=" * 40)
