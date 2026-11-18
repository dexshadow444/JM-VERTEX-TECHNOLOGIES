import re
import json

with open('assets_chunks/Blog-Du_sNO4S.js', 'r', encoding='utf-8', errors='ignore') as f:
    blog_c = f.read()

# look for array of blog posts
print("Length of Blog chunk:", len(blog_c))
posts = re.findall(r'\{id:[^}]+title:[^}]+category:[^}]+\}', blog_c)
print(f"Blog posts found ({len(posts)}):")
for p in posts[:5]:
    print(p)
