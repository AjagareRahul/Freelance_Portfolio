import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

# Now check cloudinary config
import cloudinary
print('cloudinary config after settings setup:')
print(' cloud_name:', cloudinary.config().cloud_name)
print(' api_key:', cloudinary.config().api_key)
print(' api_secret:', cloudinary.config().api_secret)

# Also from cloudinary_storage app_settings
from cloudinary_storage import app_settings
print('\nCLOUDINARY_STORAGE dict:', app_settings.user_settings)
print('MEDIA_TAG:', app_settings.MEDIA_TAG)
print('PREFIX:', app_settings.PREFIX)

# Try to get storage class
from cloudinary_storage.storage import MediaCloudinaryStorage
storage = MediaCloudinaryStorage()
print('\nStorage instance created')
print(' TAG:', storage.TAG)
print(' RESOURCE_TYPE:', storage.RESOURCE_TYPE)

# generate a URL for a test name
test_url = storage.url('test.jpg')
print(' test URL:', test_url)
