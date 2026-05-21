import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

import cloudinary
import cloudinary.uploader
from cloudinary_storage.storage import MediaCloudinaryStorage
from django.conf import settings

# Configure
cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

storage = MediaCloudinaryStorage()
print('Storage configured')

# Let's see what's already in Cloudinary
try:
    # List all resources with media tag
    result = cloudinary.api.resources(
        resource_type='image',
        prefix='media/',
        max_results=50
    )
    resources = result.get('resources', [])
    print(f'\nExisting Cloudinary images ({len(resources)}):')
    for r in resources:
        public_id = r.get('public_id')
        url = r.get('secure_url')
        print(f'  {public_id}')
        print(f'    {url}')
except Exception as e:
    print('Error listing resources:', e)

# Check what database has
from portfolio.models import Project, Gallery, UpcomingProject
print('\nDatabase records:')
for p in Project.objects.all():
    print(f'  Project: {p.title} -> image: {p.image} (type: {type(p.image).__name__})')
for g in Gallery.objects.all():
    print(f'  Gallery: {g.title} -> image: {g.image}')
for u in UpcomingProject.objects.all():
    print(f'  Upcoming: {u.title} -> image: {u.image}')
