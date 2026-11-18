import re

with open('index.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Let's search for route definitions, e.g. path:
matches = re.finditer(r'path:\s*["\']([^"\']*)["\']', c)
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(c), m.end() + 100)
    print(c[start:end])
    print("-" * 50)
