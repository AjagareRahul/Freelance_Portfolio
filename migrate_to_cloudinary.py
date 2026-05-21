import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

import cloudinary
import cloudinary.uploader
from django.conf import settings
from portfolio.models import Project, Gallery, UpcomingProject

# Configure Cloudinary
cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

print('=== Migrating local images to Cloudinary ===')

MEDIA_ROOT = settings.MEDIA_ROOT
print(f'MEDIA_ROOT: {MEDIA_ROOT}')

def upload_and_update(instance, field_name, folder_prefix=''):
    """Upload local file to Cloudinary and update model field"""
    field = getattr(instance, field_name)
    if not field:
        print(f'  {field_name} is empty, skipping')
        return False
    
    local_path = field.name  # e.g., 'projects/rawmaterailimg.png'
    full_path = os.path.join(MEDIA_ROOT, local_path)
    
    if not os.path.exists(full_path):
        print(f'  File not found locally: {full_path}')
        return False
    
    # Upload to Cloudinary
    try:
        print(f'  Uploading {local_path}...')
        with open(full_path, 'rb') as f:
            # Use folder structure in Cloudinary
            upload_result = cloudinary.uploader.upload(
                f,
                folder=folder_prefix if folder_prefix else os.path.dirname(local_path),
                use_filename=True,
                unique_filename=False,
                overwrite=True
            )
        public_id = upload_result['public_id']
        print(f'  Uploaded! Public ID: {public_id}')
        
        # Update the model field with the new public_id
        setattr(instance, field_name, public_id)
        instance.save(update_fields=[field_name])
        print(f'  Updated {field_name} to {public_id}')
        return True
    except Exception as e:
        print(f'  Error uploading {local_path}: {e}')
        return False

# Migrate Project images
print('\nProjects:')
for proj in Project.objects.all():
    print(f'  {proj.title}')
    upload_and_update(proj, 'image', 'projects')

# Migrate Gallery images
print('\nGallery:')
for img in Gallery.objects.all():
    print(f'  {img.title}')
    upload_and_update(img, 'image', 'gallery')

# Migrate UpcomingProject images
print('\nUpcoming Projects:')
for up in UpcomingProject.objects.all():
    print(f'  {up.title}')
    upload_and_update(up, 'image', 'upcoming_projects')

print('\nDone!')
