import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

import cloudinary
import cloudinary.uploader
from cloudinary_storage.storage import MediaCloudinaryStorage
from portfolio.models import Project, Gallery, UpcomingProject

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

storage = MediaCloudinaryStorage()

print('=== Checking database image fields ===')
for p in Project.objects.all():
    print(f'\nProject: {p.title}')
    print(f'  image field: {p.image}')
    print(f'  image.name: {p.image.name}')
    if p.image:
        try:
            url = p.image.url
            print(f'  URL: {url}')
            # Check existence
            exists = storage.exists(p.image.name)
            print(f'  exists in Cloudinary: {exists}')
        except Exception as e:
            print(f'  URL error: {e}')

print('\n=== Testing Cloudinary delete ===')
# Get first project
proj = Project.objects.first()
if proj and proj.image:
    name = proj.image.name
    print(f'Will delete: {name}')
    confirm = input(f'Delete {name} from Cloudinary? (yes/no): ')
    if confirm.lower() == 'yes':
        try:
            result = storage.delete(name)
            print(f'Delete result: {result}')
        except Exception as e:
            print(f'Delete error: {e}')