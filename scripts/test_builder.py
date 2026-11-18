import json
import os

with open('all_page_curricula.json', 'r', encoding='utf-8') as f:
    curricula = json.load(f)

with open('all_blog_posts_full.json', 'r', encoding='utf-8') as f:
    blogs = json.load(f)

print("Loaded curricula for", len(curricula), "pages and", len(blogs), "blogs.")
