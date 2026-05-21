import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

from portfolio.models import Project, Gallery, UpcomingProject
from cloudinary.uploader import destroy
import cloudinary

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

print('=== Fixing image field paths ===')
print('Current values (should have media/ prefix):')

for p in Project.objects.all():
    print(f'Project {p.id}: {p.image.name}')
    if p.image and not p.image.name.startswith('media/'):
        new_name = f"media/{p.image.name}"
        print(f'  -> updating to: {new_name}')
        # Direct DB update to avoid triggering storage upload
        Project.objects.filter(id=p.id).update(image=new_name)

for g in Gallery.objects.all():
    print(f'Gallery {g.id}: {g.image.name}')
    if g.image and not g.image.name.startswith('media/'):
        new_name = f"media/{g.image.name}"
        print(f'  -> updating to: {new_name}')
        Gallery.objects.filter(id=g.id).update(image=new_name)

for u in UpcomingProject.objects.all():
    print(f'Upcoming {u.id}: {u.image.name}')
    if u.image and not u.image.name.startswith('media/'):
        new_name = f"media/{u.image.name}"
        print(f'  -> updating to: {new_name}')
        UpcomingProject.objects.filter(id=u.id).update(image=new_name)

print('\nUpdate complete')

# Verify
print('\nVerifying URLs:')
from cloudinary_storage.storage import MediaCloudinaryStorage
storage = MediaCloudinaryStorage()
for p in Project.objects.all():
    if p.image:
        url = storage.url(p.image.name)
        print(f'{p.title}: {url}')
