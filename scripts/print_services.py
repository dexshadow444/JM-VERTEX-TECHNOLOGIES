import json

with open('services_curriculum_breakdown.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, v in data.items():
    print(f"=== {k} ===")
    for item in v[:12]:
        print("  -", item)
