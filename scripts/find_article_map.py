import re

with open('assets_chunks/Article-CqvRaKgq.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

print("Length of Article:", len(c))
# Let's search for how the content map is structured
# find any object with final-year-project-ideas
pos = c.find('final-year-project-ideas')
if pos != -1:
    print("Found 'final-year-project-ideas' at position:", pos)
    print(c[pos-50:pos+350])
else:
    print("'final-year-project-ideas' not found directly, finding other words...")
    words = ['Project Ideas', 'tuition fees', 'Goethe', 'MERN Stack']
    for w in words:
        p = c.find(w)
        if p != -1:
            print(f"Found '{w}' at {p}:", c[p-40:p+150])
