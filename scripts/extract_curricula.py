import glob
import re
import json

targets = [
    'WebsiteDevelopment-Dy7g2S6i.js',
    'StudentProjects-DSBfqfXe.js',
    'InternshipTraining-WhunAKGT.js',
    'GermanCourse-BxKjTn7l.js',
    'JapaneseCourse-Bfq_Fzi4.js',
    'AiTraining-4BUvsypT.js',
    'CloudComputingTraining-CCogbr-j.js',
    'CybersecurityTraining-CCdoJn0a.js',
    'DataScienceTraining-D1FFroA3.js',
    'FullStackTraining-Cdv0vwyO.js',
    'ProjectCategories-tkNRZ6pv.js',
    'Contact-DuFh3OiI.js'
]

full_details = {}

for t in targets:
    fname = t.split('-')[0]
    with open(f'assets_chunks/{t}', 'r', encoding='utf-8', errors='ignore') as f:
        code = f.read()
    
    # extract title, description, headline, subheadline
    title = re.search(r'title:\s*[`"\']([^`"\']+)[\'"`]', code)
    desc = re.search(r'description:\s*[`"\']([^`"\']+)[\'"`]', code)
    headline = re.search(r'headline:[^,]+children:\[[`"\']([^`"\']*)[\'"`]', code)
    subhead = re.search(r'subheadline:\s*[`"\']([^`"\']+)[\'"`]', code)
    
    # extract features
    features = re.findall(r'title:\s*[`"\']([^`"\']+)[\'"`],\s*description:\s*[`"\']([^`"\']+)[\'"`]', code)
    
    # extract steps
    steps = re.findall(r'title:\s*[`"\']([^`"\']+)[\'"`],\s*description:\s*[`"\']([^`"\']+)[\'"`]', code)
    
    # extract benefits
    benefits = re.findall(r'title:\s*[`"\']([^`"\']+)[\'"`],\s*desc:\s*[`"\']([^`"\']+)[\'"`]', code)
    
    full_details[fname] = {
        "seo_title": title.group(1) if title else "",
        "seo_desc": desc.group(1) if desc else "",
        "subheadline": subhead.group(1) if subhead else "",
        "features": features,
        "benefits": benefits
    }

with open('all_page_curricula.json', 'w', encoding='utf-8') as out:
    json.dump(full_details, out, indent=2)

print("Saved all curricula successfully.")
