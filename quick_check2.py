import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

from django.conf import settings

print('Django version:', django.get_version())
print('DEFAULT_FILE_STORAGE:', settings.DEFAULT_FILE_STORAGE)

import django.core.files.storage as storage_module
print('Available in storage module:', [x for x in dir(storage_module) if not x.startswith('_')])

from django.core.files.storage import default_storage
print('default_storage class:', default_storage.__class__.__name__)
print('default_storage module:', default_storage.__class__.__module__)

# Let's also check what storage class is returned for the string
from django.core.files.storage import Storage
# Since get_storage_class may not be directly importable, import from django.core.files.storage import get_storage_class fails?
# Actually, check:
try:
    from django.core.files.storage import get_storage_class
    print('get_storage_class available')
except ImportError as e:
    print('get_storage_class NOT available:', e)

# Try to import manually
from django.core.files import storage
print('storage.get_storage_class?', hasattr(storage, 'get_storage_class'))
if hasattr(storage, 'get_storage_class'):
    get_storage_class = storage.get_storage_class
    cls = get_storage_class(settings.DEFAULT_FILE_STORAGE)
    print('Resolved storage class:', cls)
