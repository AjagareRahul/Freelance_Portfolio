import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.core.files.base import ContentFile
import cloudinary

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

storage = RawMediaCloudinaryStorage()

# Create a dummy text file as content (pdf mimetype but we don't need a real pdf for test)
content = ContentFile(b'%PDF-1.4 fake pdf content for testing', name='test.pdf')
public_id = storage.save('pdf_test', content)
print('Saved public_id:', public_id)
url = storage.url(public_id)
print('URL:', url)

import requests
resp = requests.head(url, timeout=10)
print('HEAD status:', resp.status_code)
resp2 = requests.get(url, timeout=10)
print('GET status:', resp2.status_code, 'len', len(resp2.content))
