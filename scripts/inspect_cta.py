import re
import json

with open('assets_chunks/CallToAction-Ca8bqmom.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Let's find arrays of objects
# e.g., features, courses, syllabus, steps
matches = re.findall(r'[`"\']([A-Z][^`"\']{15,200})[`"\']', c)
clean = []
for m in matches:
    if not any(skip in m for skip in ['React', 'Element', 'HTML', 'Error', 'Warning', 'Cannot', 'useMemo', 'useState', 'useEffect']):
        clean.append(m)

print(f"Total phrases found in CallToAction chunk: {len(clean)}")
# Print samples
for item in clean[:40]:
    print("-", item)
