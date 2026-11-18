import urllib.request
import re
import os
import json

base_url = "https://jmvertextechnologies.com/assets/"

with open('index.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

chunks = list(set(re.findall(r'[\w\.-]+\.js', text)))
# Filter out non-asset chunks
chunks = [c for c in chunks if '-' in c and not c.startswith('http')]

os.makedirs('assets_chunks', exist_ok=True)

print(f"Total chunks found: {len(chunks)}")
downloaded = {}

for chunk in chunks:
    url = base_url + chunk
    chunk_path = os.path.join('assets_chunks', chunk)
    try:
        urllib.request.urlretrieve(url, chunk_path)
        with open(chunk_path, 'r', encoding='utf-8', errors='ignore') as cf:
            content = cf.read()
        downloaded[chunk] = content
        print(f"Downloaded {chunk} ({len(content)} bytes)")
    except Exception as e:
        print(f"Failed {chunk}: {e}")

# Now let's extract routes from index.js
# React router routes typically look like {path:"/services", element:...}
routes_pattern = re.findall(r'path:\s*["\']([^"\']+)["\']', text)
print("Routes in index.js:", set(routes_pattern))

# Let's inspect each downloaded chunk for readable text, titles, headings, descriptions
analysis = {}

for name, content in downloaded.items():
    page_name = name.split('-')[0]
    
    # Extract titles, descriptions, headings
    # look for strings between quotes
    raw_strings = re.findall(r'["\']([^"\']{15,500})["\']', content)
    # clean out code artifacts
    filtered = [s for s in raw_strings if not re.search(r'[{}\[\]<>=;]|function|return|import|export|class|var|let|const', s)]
    
    # Extract bullet points, items, arrays
    analysis[page_name] = {
        "chunk_file": name,
        "sample_content": filtered[:25]
    }

with open("site_analysis_extracted.json", "w", encoding="utf-8") as out:
    json.dump(analysis, out, indent=2)

print("Saved extraction to site_analysis_extracted.json")
