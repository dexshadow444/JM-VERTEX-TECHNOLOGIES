import re
import json

def inspect_file(fname):
    with open(f'assets_chunks/{fname}', 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    return c

# 1. Portfolio
port_c = inspect_file('Portfolio-rWY8tyJN.js')
print("=== PORTFOLIO ===")
port_items = re.findall(r'\{id:[^}]+title:[^}]+category:[^}]+\}', port_c)
if not port_items:
    port_items = re.findall(r'\{[^{}]*title:[^{}]*category:[^{}]*\}', port_c)
for pi in port_items:
    print(pi)
if not port_items:
    # print string literals
    print(re.findall(r'[`"\']([^`"\']{6,100})[`"\']', port_c)[:20])

# 2. FAQs
faq_c = inspect_file('FAQ-CfIOuf05.js')
print("\n=== FAQS ===")
faqs = re.findall(r'\{question:[^}]+answer:[^}]+\}', faq_c)
for fq in faqs:
    print(fq)

# 3. Blog
blog_c = inspect_file('Blog-Du_sNO4S.js')
print("\n=== BLOG POSTS ===")
blogs = re.findall(r'\{id:[^}]+title:[^}]+excerpt:[^}]+\}', blog_c)
for bg in blogs:
    print(bg)
