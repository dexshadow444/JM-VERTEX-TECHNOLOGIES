import re
import json

with open('assets_chunks/Article-CqvRaKgq.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Let's inspect how articles are keyed or structured
# Often it's an object with article IDs as keys: { 'final-year-project-ideas': { title: ... } }
keys = re.findall(r'[`"\']([a-z0-9\-]+)[`"\']\s*:\s*\{', c)
print("Article Keys found:", keys)

# Let's also look for title: in Article chunk
titles = re.findall(r'title:\s*[`"\']([^`"\']+)[\'"`]', c)
print(f"Titles found in Article ({len(titles)}):", titles[:10])
