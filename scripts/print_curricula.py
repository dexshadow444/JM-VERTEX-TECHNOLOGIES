import json

with open('all_page_curricula.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for k, v in d.items():
    print(f"=== {k} ===")
    print("SEO Title:", v['seo_title'])
    print("SEO Desc:", v['seo_desc'])
    print("Subheadline:", v['subheadline'])
    print("Features count:", len(v['features']))
    for f_title, f_desc in v['features'][:6]:
        print(f"  * {f_title}: {f_desc}")
    print("Benefits count:", len(v['benefits']))
    for b_title, b_desc in v['benefits'][:6]:
        print(f"  + {b_title}: {b_desc}")
    print()
