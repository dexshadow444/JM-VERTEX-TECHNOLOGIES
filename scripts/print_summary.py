import json

with open('full_site_content_summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, v in data.items():
    print(f"==================== {k} ====================")
    for item in v[:15]:
        print("  *", item)
