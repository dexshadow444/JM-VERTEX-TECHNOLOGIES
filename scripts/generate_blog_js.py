import json

with open('all_blog_posts_full.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

js_content = "/**\n * JM VERTEX TECHNOLOGIES — Official Technical Publications & Research Archive\n * 20 Comprehensive Industry Guides & Academic Articles\n */\n\n"
js_content += "window.JM_BLOG_POSTS = " + json.dumps(posts, indent=2) + ";\n"

with open('assets/js/blog-data.js', 'w', encoding='utf-8') as out:
    out.write(js_content)

print("Generated assets/js/blog-data.js with", len(posts), "posts.")
