import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

from django.conf import settings

print('=== Testing Cloudinary Storage Import ===')
try:
    from cloudinary_storage.storage import MediaCloudinaryStorage
    print('Imported MediaCloudinaryStorage successfully')
    print('Class:', MediaCloudinaryStorage)
    
    # Try instantiate
    storage = MediaCloudinaryStorage()
    print('Instance created:', storage)
    print('cloud_name:', getattr(storage, 'cloud_name', 'N/A'))
    print('API key present:', bool(getattr(storage, 'api_key', None)))
except Exception as e:
    print('Failed to import/instantiate:', e)
    import traceback
    traceback.print_exc()

# Now check default_storage
from django.core.files.storage import default_storage
print('\ndefault_storage class:', default_storage.__class__.__name__)
print('default_storage module:', default_storage.__class__.__module__)

# Let's explicitly get storage class via Django's mechanism
from django.core.files.storage import get_storage_class
try:
    StorageCls = get_storage_class(settings.DEFAULT_FILE_STORAGE)
    print('\nget_storage_class returned:', StorageCls)
    instance = StorageCls()
    print('Instance class:', instance.__class__.__name__)
except Exception as e:
    print('get_storage_class error:', e)
