import glob
import re
import json

targets = [
    'PythonTraining-BmBlP_ZD.js',
    'FullStackTraining-Cdv0vwyO.js',
    'CloudComputingTraining-CCogbr-j.js',
    'AiTraining-4BUvsypT.js',
    'CybersecurityTraining-CCdoJn0a.js',
    'DataScienceTraining-D1FFroA3.js',
    'GermanCourse-BxKjTn7l.js',
    'JapaneseCourse-Bfq_Fzi4.js',
    'WebsiteDevelopment-Dy7g2S6i.js',
    'StudentProjects-DSBfqfXe.js',
    'InternshipTraining-WhunAKGT.js',
    'Contact-DuFh3OiI.js'
]

results = {}
for t in targets:
    try:
        with open(f'assets_chunks/{t}', 'r', encoding='utf-8', errors='ignore') as f:
            code = f.read()
        strings = re.findall(r'[`"\']([^`"\']{10,400})[`"\']', code)
        clean = []
        for s in strings:
            if not any(b in s for b in ['stroke-', 'M12', 'viewBox', 'xmlns', 'http://www.w3.org', 'style', 'class', 'px', 'calc(']):
                clean.append(s.strip())
        seen = set()
        dedup = [s for s in clean if not (s in seen or seen.add(s))]
        results[t.split('-')[0]] = dedup
    except Exception as e:
        results[t] = str(e)

with open('services_curriculum_breakdown.json', 'w', encoding='utf-8') as out:
    json.dump(results, out, indent=2)

print("Saved detailed services curriculum breakdown.")
