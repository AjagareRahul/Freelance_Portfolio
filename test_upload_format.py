import cloudinary
import cloudinary.uploader
import os
from io import BytesIO
from PIL import Image

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

# Create a tiny test image
img = Image.new('RGB', (10, 10), color='red')
buffer = BytesIO()
img.save(buffer, format='PNG')
buffer.seek(0)

print('Uploading test image to Cloudinary with use_filename=True...')
result = cloudinary.uploader.upload(
    buffer,
    folder='projects',
    use_filename=True,
    unique_filename=False,
    overwrite=True
)
print('Public ID:', result['public_id'])
print('URL:', result['secure_url'])
print('Full response:', result)