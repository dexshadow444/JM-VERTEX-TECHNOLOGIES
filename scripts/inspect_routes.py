import re

with open('index.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

paths = re.findall(r'path:"([^"]+)"', c)
print('path: matches:', paths)

routes = re.findall(r'"(/[a-zA-Z0-9_\-/]*)"', c)
clean_routes = sorted(list(set([r for r in routes if len(r) > 1 and '.' not in r])))
print('Clean url paths in index.js:', clean_routes)

# Also look for navigation items in CallToAction-Ca8bqmom.js or Home-i-Cc6tga.js
with open('assets_chunks/CallToAction-Ca8bqmom.js', 'r', encoding='utf-8', errors='ignore') as f:
    cta = f.read()

cta_routes = re.findall(r'"(/[a-zA-Z0-9_\-/]*)"', cta)
print('Clean url paths in CallToAction:', sorted(list(set([r for r in cta_routes if len(r) > 1 and '.' not in r]))))
