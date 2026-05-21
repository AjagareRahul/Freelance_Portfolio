import django
from django.conf import settings

print('Django version:', django.get_version())
print('DEFAULT_FILE_STORAGE:', settings.DEFAULT_FILE_STORAGE)

import django.core.files.storage as storage_module
print('Available in storage module:', [x for x in dir(storage_module) if not x.startswith('_')])
