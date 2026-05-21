import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from cloudinary_storage.storage import MediaCloudinaryStorage
from django.core.files.base import ContentFile
import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

storage = MediaCloudinaryStorage()

# Create a simple PDF-like content (not a real PDF, but Cloudinary may accept)
content = b'%PDF-1.4 fake content'
cf = ContentFile(content, name='fake.pdf')
name = storage.save('test_pdf_file', cf)
print('Saved name:', name)
url = storage.url(name)
print('URL:', url)

# Check access
import requests
r = requests.head(url, timeout=10)
print('HEAD status:', r.status_code)

# Now try raw storage
from cloudinary_storage.storage import RawMediaCloudinaryStorage
raw_storage = RawMediaCloudinaryStorage()
name2 = raw_storage.save('test_raw_pdf', cf)
print('Raw saved name:', name2)
url2 = raw_storage.url(name2)
print('Raw URL:', url2)
r2 = requests.head(url2, timeout=10)
print('Raw HEAD status:', r2.status_code)
