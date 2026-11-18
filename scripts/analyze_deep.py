import re
import json

with open('index.js', 'r', encoding='utf-8', errors='ignore') as f:
    js = f.read()

print("JS bundle size:", len(js), "bytes")

# Find strings
# Let's see what components or data objects are declared
# Often React apps have arrays of objects for services, features, testimonials, faqs, navigation links

# Let's search for navigation items
nav_matches = re.findall(r'(\{[^{}]*label[^{}]*\})', js)
print(f"Found {len(nav_matches)} items with 'label'")
for m in nav_matches[:10]:
    print("NAV/LABEL ITEM:", m)

# Find sections / ids
section_ids = re.findall(r'id:\s*["\']([a-zA-Z0-9_-]+)["\']', js)
print("Section IDs:", set(section_ids))

# Find hrefs to anchors or paths
anchors = re.findall(r'href:\s*["\'](#[a-zA-Z0-9_-]+)["\']', js)
print("Anchor links:", set(anchors))

paths = re.findall(r'to:\s*["\']([^"\']+)["\']', js)
print("Router links (to):", set(paths))

# Let's find large text blocks, headers, service descriptions
paragraphs = re.findall(r'["\']([A-Z][^"\']{30,250})["\']', js)
print(f"Found {len(paragraphs)} long text sentences. Sampling 20:")
for p in paragraphs[:25]:
    if not p.startswith("http") and not "<" in p and not "\\" in p[:5]:
        print(" -", p)
