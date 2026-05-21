import os
import sys

# Add project to path
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

from django.conf import settings

print('=== Django Settings Check ===')
print(f'DEFAULT_FILE_STORAGE: {settings.DEFAULT_FILE_STORAGE}')
print(f'MEDIA_URL: {settings.MEDIA_URL}')
print(f'CLOUDINARY_SDK_AVAILABLE: {settings.CLOUDINARY_SDK_AVAILABLE}')
print(f'CLOUDINARY_CLOUD_NAME: {settings.CLOUDINARY_CLOUD_NAME}')
print(f'CLOUDINARY_API_KEY present: {bool(settings.CLOUDINARY_API_KEY)}')
print(f'CLOUDINARY_API_SECRET present: {bool(settings.CLOUDINARY_API_SECRET)}')

# Check a sample model field
from portfolio.models import SiteInfo
site = SiteInfo.objects.first()
if site and site.profile_image:
    print(f'Profile image URL: {site.profile_image.url}')
    print(f'Profile image name: {site.profile_image.name}')
else:
    print('No profile image in database')
