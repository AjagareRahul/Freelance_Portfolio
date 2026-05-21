import cloudinary
import cloudinary.uploader
import cloudinary.api
cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

# Create a minimal fake PDF content (not a real PDF but just to test delivery)
content = b'%PDF-1.4 fake pdf content'
from io import BytesIO
from django.core.files.base import ContentFile
cf = ContentFile(content)

# Upload using resource_type='raw'
result = cloudinary.uploader.upload(cf, folder='test_raw', resource_type='raw')
print('Uploaded with raw:', result['public_id'], result.get('secure_url'))

# Now check via API
info = cloudinary.api.resource(result['public_id'], resource_type='raw')
print('Access mode:', info.get('access_mode'))
print('Secure URL:', info.get('secure_url'))

# Try to GET that URL
import requests
resp = requests.get(info['secure_url'], timeout=10)
print('GET status:', resp.status_code)
print('Content length:', len(resp.content))
