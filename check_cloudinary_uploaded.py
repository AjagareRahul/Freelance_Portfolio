import cloudinary
import cloudinary.uploader
import os

# Use the credentials from .env
cloudinary.config(
    cloud_name='Root',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)

print('Cloudinary configured')
print('Cloud name:', cloudinary.config().cloud_name)

# List resources in the account
try:
    result = cloudinary.api.resources(
        resource_type='image',
        prefix='media/',
        max_results=10
    )
    print('Resources found:', len(result.get('resources', [])))
    for res in result.get('resources', [])[:5]:
        print(f"  - {res.get('public_id')} (format: {res.get('format')})")
        print(f"    URL: {res.get('secure_url')}")
except Exception as e:
    print('Error listing resources:', e)

# Also try to get info about a specific expected image
test_public_id = 'projects/rawmaterailimg'
try:
    info = cloudinary.uploader.explicit(test_public_id, type='upload')
    print(f'\nFound by public_id: {info}')
except Exception as e:
    print(f'\nNot found by public_id {test_public_id}: {e}')
