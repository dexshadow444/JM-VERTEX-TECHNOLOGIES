import re

with open('index.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Look for react router components or imports
print("Length of index.js:", len(c))
# Look for substrings like Route, Link, BrowserRouter, or router
matches = [m.start() for m in re.finditer(r'Route|Link|Router|href|navigate|window\.location', c)]
print("Route/Router keyword hits:", len(matches))

# Let's inspect around first 5 hits
for idx in matches[:10]:
    start = max(0, idx - 80)
    end = min(len(c), idx + 80)
    print("MATCH:", c[start:end])
    print("="*40)
