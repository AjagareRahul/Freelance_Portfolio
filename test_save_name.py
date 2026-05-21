import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

import cloudinary
import cloudinary.uploader
from cloudinary_storage.storage import MediaCloudinaryStorage
from io import BytesIO
from PIL import Image

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

storage = MediaCloudinaryStorage()

# Create a test image
img = Image.new('RGB', (5,5), color='blue')
buffer = BytesIO()
img.save(buffer, format='PNG')
buffer.seek(0)

# Simulate saving a file with name like 'projects/test.png'
from django.core.files.base import ContentFile
content = ContentFile(buffer.read())
# Use storage's _save method directly
name = 'projects/test.png'
saved_name = storage._save(name, content)
print('Saved name (public_id):', saved_name)
print('Generated URL:', storage.url(saved_name))

# Also test with full path including 'media/' prefix to see effect
content2 = ContentFile(buffer.read())
saved_name2 = storage._save('media/projects/test2.png', content2)
print('With media prefix saved name:', saved_name2)
print('URL:', storage.url(saved_name2))
