import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

from portfolio.models import Project, SiteInfo, Gallery, UpcomingProject
from django.conf import settings

print('=== Image URL Check (post Cloudinary config) ===')
print('Default storage:', settings.STORAGES['default']['BACKEND'])

proj = Project.objects.first()
if proj and proj.image:
    print(f'Project: {proj.title}, image.name: {proj.image.name}')
    print('image.url:', proj.image.url)
else:
    print('No project with image')

gallery = Gallery.objects.first()
if gallery and gallery.image:
    print(f'Gallery: {gallery.title}, image.url: {gallery.image.url}')

upcoming = UpcomingProject.objects.first()
if upcoming and upcoming.image:
    print(f'Upcoming: {upcoming.title}, image.url: {upcoming.image.url}')
else:
    print('Upcoming: none with image')