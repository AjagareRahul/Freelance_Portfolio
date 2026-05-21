import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

# BEFORE django.setup(), check env vars
print('Env vars before setup:')
print('  CLOUDINARY_CLOUD_NAME:', os.environ.get('CLOUDINARY_CLOUD_NAME'))
print('  CLOUDINARY_API_KEY:', os.environ.get('CLOUDINARY_API_KEY'))
print('  CLOUDINARY_API_SECRET:', os.environ.get('CLOUDINARY_API_SECRET'))

import django
django.setup()

from django.conf import settings
print('\nAfter setup:')
print('  DEFAULT_FILE_STORAGE:', settings.DEFAULT_FILE_STORAGE)
print('  STORAGES:', getattr(settings, 'STORAGES', 'Not defined'))
print('  CLOUDINARY_CLOUD_NAME:', settings.CLOUDINARY_CLOUD_NAME)

from django.core.files.storage import default_storage
print('\ndefault_storage class:', default_storage.__class__.__name__)
print('default_storage module:', default_storage.__class__.__module__)

from portfolio.models import SiteInfo
si = SiteInfo.objects.first()
if si and si.resume:
    print('\nSiteInfo resume field storage:', si.resume.field.storage.__class__.__name__)
    print('SiteInfo resume.url:', si.resume.url)
