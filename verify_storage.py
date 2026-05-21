import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

from django.conf import settings
from django.core.files.storage import default_storage

print('=== Settings Check ===')
print('DEFAULT_FILE_STORAGE (legacy):', getattr(settings, 'DEFAULT_FILE_STORAGE', 'Not set'))
print('STORAGES:', settings.STORAGES if hasattr(settings, 'STORAGES') else 'Not defined')
print('default_storage class:', default_storage.__class__.__name__)
print('default_storage module:', default_storage.__class__.__module__)

# Test URL generation
if hasattr(default_storage, 'url'):
    test_url = default_storage.url('test.jpg')
    print('Test URL:', test_url)
else:
    print('default_storage has no url method')