import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

from django.conf import settings
from django.core.files.storage import default_storage

print('=== Storage Diagnostics ===')
print(f'Default storage class: {default_storage.__class__.__name__}')
print(f'Default storage module: {default_storage.__class__.__module__}')

# Check if Cloudinary storage has proper base URL
if hasattr(default_storage, 'cloudinary'):
    print(f'Cloudinary config: {default_storage.cloudinary.config().cloud_name}')
else:
    print('Storage does not have cloudinary attribute')

# Test with a sample path
test_path = 'projects/test.png'
try:
    url = default_storage.url(test_path)
    print(f'Test URL for {test_path}: {url}')
except Exception as e:
    print(f'Error generating URL: {e}')

# Check actual configured storage
from cloudinary_storage.storage import MediaCloudinaryStorage
print(f'\nMediaCloudinaryStorage base URL: {MediaCloudinaryStorage()._base_url if hasattr(MediaCloudinaryStorage(), "_base_url") else "N/A"}')
# Check cloud_name
try:
    cs = MediaCloudinaryStorage()
    print(f'Storage cloud_name: {cs.cloud_name}')
except Exception as e:
    print(f'Error accessing cloud_name: {e}')
