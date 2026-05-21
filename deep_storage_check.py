import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

from django.conf import settings
from django.core.files.storage import default_storage

print('=== Inspecting default_storage internals ===')
print('type(default_storage):', type(default_storage))
# default_storage is an instance of DefaultStorage (a LazyObject)
# It has _wrapped attribute after setup
if hasattr(default_storage, '_wrapped'):
    print('_wrapped:', default_storage._wrapped)
if hasattr(default_storage, '_setup'):
    print('Calling _setup again to see what happens...')
    # Let's see what default_storage uses to set up
    # The DefaultStorage class uses get_storage_class(settings.DEFAULT_FILE_STORAGE)
    # We can import get_storage_class
try:
    from django.core.files.storage import get_storage_class
    print('get_storage_class available')
except ImportError:
    # In newer Django, it's maybe storage.get_storage_class
    from django.core.files import storage as st
    get_storage_class = st.get_storage_class
    print('got get_storage_class from storage module')

StorageCls = get_storage_class(settings.DEFAULT_FILE_STORAGE)
print('Storage class from DEFAULT_FILE_STORAGE:', StorageCls)

# instantiate and see url method
storage = StorageCls()
print('storage instance class:', storage.__class__.__name__)
print('storage instance url method:', storage.url)

# Also print actual setting value
print('\nsettings.DEFAULT_FILE_STORAGE =', settings.DEFAULT_FILE_STORAGE)
