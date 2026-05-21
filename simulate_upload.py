import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from django.core.files.base import ContentFile
from portfolio.models import Project
from cloudinary_storage.storage import MediaCloudinaryStorage
import cloudinary

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

storage = MediaCloudinaryStorage()

# Simulate admin upload for project
proj = Project.objects.first()
print(f'Project: {proj.title}')

# Read a real image file from local if available
# Check if any local image exists for this project
local_path = r'D:\Freelance_Portfolio\media\projects\rawmaterailimg.png'
if os.path.exists(local_path):
    with open(local_path, 'rb') as f:
        content = ContentFile(f.read())
    # Simulate field.save() like in admin
    field = proj.image
    new_name = storage.save('projects/rawmaterailimg.png', content)
    print('Saved to Cloudinary, new name (public_id):', new_name)
    # Update DB
    proj.image = new_name
    proj.save()
    print('Project image updated to:', proj.image.name)
    print('URL:', proj.image.url)
else:
    print(f'Local file missing: {local_path}')
    print('Need the original image file to upload.')
