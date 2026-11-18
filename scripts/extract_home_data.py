import re
import json

with open('assets_chunks/Home-i-Cc6tga.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Let's extract object arrays inside Home
# 1. Team members (Q)
team_matches = re.findall(r'\{initials:[^}]+whatsappNum:[^}]+\}', c)
print("Team matches:")
for tm in team_matches:
    print(tm)

# 2. Testimonials (X)
test_matches = re.findall(r'\{name:[^}]+feedback:[^}]+\}', c)
print("\nTestimonial matches:")
for tm in test_matches:
    print(tm)

# 3. Student achievements (Z)
achieve_matches = re.findall(r'\{name:[^}]+achievement:[^}]+\}', c)
print("\nAchievement matches:")
for am in achieve_matches:
    print(am)

# 4. Service cards in U
services_matches = re.findall(r'\{id:[^}]+title:[^}]+description:[^}]+\}', c)
print("\nService matches in U:")
for sm in services_matches:
    print(sm)
