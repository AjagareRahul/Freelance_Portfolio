import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import Project, Gallery, UpcomingProject
from cloudinary_storage.storage import MediaCloudinaryStorage
import cloudinary

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

storage = MediaCloudinaryStorage()

print('=== Project Images ===')
for p in Project.objects.all():
    name = p.image.name
    print(f'{p.title}: {name}')
    if name:
        # Generate URL
        url = storage.url(name)
        print(f'  URL: {url}')
        # Check existence on Cloudinary
        try:
            exists = storage.exists(name)
            print(f'  exists: {exists}')
        except Exception as e:
            print(f'  exists check error: {e}')

print('\n=== Gallery Images ===')
for g in Gallery.objects.all():
    name = g.image.name
    print(f'{g.title}: {name}')
    if name:
        url = storage.url(name)
        print(f'  URL: {url}')
        try:
            exists = storage.exists(name)
            print(f'  exists: {exists}')
        except Exception as e:
            print(f'  exists error: {e}')

print('\n=== Upcoming Projects ===')
for u in UpcomingProject.objects.all():
    name = u.image.name
    print(f'{u.title}: {name}')
    if name:
        url = storage.url(name)
        print(f'  URL: {url}')
        try:
            exists = storage.exists(name)
            print(f'  exists: {exists}')
        except Exception as e:
            print(f'  exists error: {e}')
