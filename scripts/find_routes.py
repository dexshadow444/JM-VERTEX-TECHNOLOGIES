import glob
import re
import json

# Check where Navbar, Footer, and Routes are defined
files = glob.glob('assets_chunks/*.js') + ['index.js']

for fpath in files:
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    
    # check if path: or router is here
    if 'path:' in c or 'path :' in c or 'createBrowserRouter' in c or 'BrowserRouter' in c or 'Routes' in c:
        print(f"Router found in: {fpath}")
        routes = re.findall(r'path:\s*["\']([^"\']+)["\']', c)
        if routes:
            print(f"  Routes in {fpath}:", routes)

    # Check for email, phone, location
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', c)
    phones = re.findall(r'\+?\d{2,4}[- ]?\d{5}[- ]?\d{5}', c)
    if emails:
        print(f"Emails in {fpath}:", set(emails))
    if phones:
        print(f"Phones in {fpath}:", set(phones))
