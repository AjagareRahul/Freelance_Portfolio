import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

import django.core.files.storage as storage_module
print('storage module contents:')
for name in dir(storage_module):
    if not name.startswith('_'):
        print(' ', name)

# inspect default_storage object itself
from django.core.files.storage import default_storage
print('\ndefault_storage object:', default_storage)
print('default_storage.__class__:', default_storage.__class__)
print('Is LazyObject?', type(default_storage).__name__)

# Try to force evaluation
print('\nForcing evaluation by calling ._setup...')
# In Django, default_storage is a LazyObject; _setup() loads the actual storage.
# But we can access ._wrapped or call ._setup if present.
if hasattr(default_storage, '_setup'):
    print('LazyObject has _setup')
    default_storage._setup()
print('After setup, class:', default_storage.__class__.__name__)
print('After setup, module:', default_storage.__class__.__module__)
