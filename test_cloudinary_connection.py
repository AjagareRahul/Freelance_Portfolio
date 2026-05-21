import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

import cloudinary
import cloudinary.uploader

# Configure with new credentials
cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

print('Testing Cloudinary connection...')
try:
    # List resources to verify connection
    result = cloudinary.api.resources(
        resource_type='image',
        max_results=5
    )
    resources = result.get('resources', [])
    print(f'Connected! Found {len(resources)} existing images in Cloudinary.')
    if resources:
        print('Sample URLs:')
        for r in resources[:3]:
            print(f"  {r.get('public_id')}: {r.get('secure_url')}")
except Exception as e:
    print('Connection error:', e)
