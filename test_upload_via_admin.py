import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import Project
from django.core.files.base import ContentFile
from io import BytesIO
from PIL import Image

img = Image.new('RGB', (10,10), color='red')
buffer = BytesIO()
img.save(buffer, format='PNG')
buffer.seek(0)
content = ContentFile(buffer.read())

proj = Project(
    title='Test Project',
    slug='test-project',
    description='Test',
    short_description='test',
    is_published=True
)
proj.image.save('test.png', content, save=False)
proj.save()
print('Saved project image:', proj.image.name)
print('URL:', proj.image.url)

# Check via storage
from django.core.files.storage import default_storage
print('Exists in Cloudinary?', default_storage.exists(proj.image.name))