import re
import json

def get_strings(code):
    # Match backticks, single quotes, double quotes
    pattern = re.compile(r'[`"\']([^`"\']{3,500})[`"\']')
    matches = pattern.findall(code)
    # clean noise
    cleaned = []
    for m in matches:
        if any(skip in m for skip in ['stroke-', 'M12', 'viewBox', 'xmlns', 'http://www.w3.org', 'style', 'class', 'px', 'calc(']):
            continue
        cleaned.append(m)
    return cleaned

# Let's inspect index.js
with open('index.js', 'r', encoding='utf-8', errors='ignore') as f:
    index_c = f.read()

# Look for dynamic import paths in index.js
imports = re.findall(r'import\([`"\'](\./[^`"\']+)[`"\']\)', index_c)
print("Dynamic imports in index.js:")
for imp in imports:
    print(" ", imp)

# Also look for path / route mapping
routes = re.findall(r'path:\s*[`"\']([^`"\']+)[`"\']', index_c)
print("Routes with path: in index.js:", routes)

# Let's search for navigation links in index.js
nav_links = re.findall(r'href:\s*[`"\']([^`"\']+)[`"\']', index_c)
print("Hrefs in index.js:", set(nav_links))

# Also search for <Route or routes array in index.js
# Let's search for router configuration
router_config = re.findall(r'path:\s*[`"\']([/a-zA-Z0-9_\-]+)[`"\']', index_c)
print("Router config paths:", router_config)
