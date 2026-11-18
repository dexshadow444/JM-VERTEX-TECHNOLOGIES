import os
import sys

# Ensure base_templates is imported
sys.path.append(os.path.abspath('.'))

# Import builders
import generate_services_pages
import generate_training_pages
import generate_language_pages
import generate_portfolio_blog
import generate_contact_system_pages

print("Rebuilding all 21 inner pages with the new studio aesthetic...")

# Re-run service pages
generate_services_pages.build_webdev()
generate_services_pages.build_student_projects()
generate_services_pages.build_project_categories()
generate_services_pages.build_internship()

# Re-run training pages
for track in generate_training_pages.TRAINING_TRACKS:
    generate_training_pages.build_training_page(track)

# Re-run language pages
generate_language_pages.build_german()
generate_language_pages.build_japanese()

# Re-run portfolio and blog
generate_portfolio_blog.build_portfolio()
generate_portfolio_blog.build_blog()
generate_portfolio_blog.build_blog_detail()

# Re-run contact and system pages
generate_contact_system_pages.build_contact()
generate_contact_system_pages.build_privacy_policy()
generate_contact_system_pages.build_terms()
generate_contact_system_pages.build_404()
generate_contact_system_pages.build_500()
generate_contact_system_pages.build_offline()

print("All 22 pages rebuilt with Studio Grade Design System!")
