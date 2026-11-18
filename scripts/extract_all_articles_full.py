import re
import json

with open('assets_chunks/Blog-Du_sNO4S.js', 'r', encoding='utf-8', errors='ignore') as f:
    blog_c = f.read()

# Extract list of blog metadata
# {id:`final-year-project-ideas`,title:`Best Final Year Project Ideas for IT Students in 2024`,excerpt:`...`,date:`Oct 15, 2023`,category:`Student Projects`}
post_regex = re.compile(r'\{id:\s*[`"\']([^`"\']+)[\'"`],\s*title:\s*[`"\']([^`"\']+)[\'"`],\s*excerpt:\s*[`"\']([^`"\']+)[\'"`],\s*date:\s*[`"\']([^`"\']+)[\'"`],\s*category:\s*[`"\']([^`"\']+)[\'"`]\}')
posts = []
for match in post_regex.finditer(blog_c):
    posts.append({
        "id": match.group(1),
        "title": match.group(2),
        "excerpt": match.group(3),
        "date": match.group(4),
        "category": match.group(5)
    })

print(f"Extracted {len(posts)} posts metadata.")

with open('assets_chunks/Article-CqvRaKgq.js', 'r', encoding='utf-8', errors='ignore') as f:
    art_c = f.read()

# For each post id, let's extract the text inside case`id`: ... break/return
for p in posts:
    pid = p['id']
    pattern = rf'case[`"\']{pid}[`"\']:(.*?)(?:case[`"\']|default:|$)'
    m = re.search(pattern, art_c, re.DOTALL)
    if m:
        block = m.group(1)
        # extract all strings inside children:
        paragraphs = re.findall(r'children:\s*[`"\']([^`"\']{10,1200})[\'"`]', block)
        if not paragraphs:
            paragraphs = re.findall(r'[`"\']([A-Z][^`"\']{15,1200})[\'"`]', block)
        # clean noise
        clean_p = [s for s in paragraphs if not any(x in s for x in ['className', 'stroke-', 'text-gray', 'M12'])]
        p['content_paragraphs'] = clean_p
    else:
        p['content_paragraphs'] = [p['excerpt']]

with open('all_blog_posts_full.json', 'w', encoding='utf-8') as out:
    json.dump(posts, out, indent=2)

print("Saved all_blog_posts_full.json successfully!")
