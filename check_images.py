import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

from portfolio.models import SiteInfo, Project, BlogPost, Gallery, Testimonial, UpcomingProject

print('=== Checking all image fields ===')

# SiteInfo
site = SiteInfo.objects.first()
if site:
    print(f'\nSiteInfo: {site}')
    print(f'  profile_image: {site.profile_image}')
    if site.profile_image:
        print(f'    URL: {site.profile_image.url}')
    print(f'  resume: {site.resume}')
    if site.resume:
        print(f'    URL: {site.resume.url}')
else:
    print('No SiteInfo found')

# Projects
projects = Project.objects.all()
print(f'\nProjects ({projects.count()}):')
for p in projects:
    print(f'  {p.title}: image={p.image}')
    if p.image:
        print(f'    URL: {p.image.url}')

# BlogPosts
blogs = BlogPost.objects.all()
print(f'\nBlogPosts ({blogs.count()}):')
for b in blogs:
    print(f'  {b.title}: image={b.image}')
    if b.image:
        print(f'    URL: {b.image.url}')

# Gallery
gallery = Gallery.objects.all()
print(f'\nGallery ({gallery.count()}):')
for g in gallery:
    print(f'  {g.title}: image={g.image}')
    if g.image:
        print(f'    URL: {g.image.url}')

# Testimonials
testimonials = Testimonial.objects.all()
print(f'\nTestimonials ({testimonials.count()}):')
for t in testimonials:
    print(f'  {t.client_name}: image={t.client_image}')
    if t.client_image:
        print(f'    URL: {t.client_image.url}')

# UpcomingProjects
upcoming = UpcomingProject.objects.all()
print(f'\nUpcomingProjects ({upcoming.count()}):')
for u in upcoming:
    print(f'  {u.title}: image={u.image}')
    if u.image:
        print(f'    URL: {u.image.url}')
