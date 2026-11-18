import re

with open('assets_chunks/FAQ-CfIOuf05.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# find questions and answers
q_matches = re.findall(r'[`"\']([^`"\']{15,300})[`"\']', c)
for q in q_matches:
    if any(k in q.lower() for k in ['?', 'jm vertex', 'project', 'training', 'internship', 'german', 'website', 'cost', 'support']):
        print("FAQ item:", q)
