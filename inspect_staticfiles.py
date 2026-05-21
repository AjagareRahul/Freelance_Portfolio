import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from django.conf import settings
print('STATICFILES_STORAGE setting:', settings.STATICFILES_STORAGE)

from django.contrib.staticfiles.storage import staticfiles_storage
print('staticfiles_storage object:', staticfiles_storage)
print('staticfiles_storage class:', staticfiles_storage.__class__.__name__)
print('staticfiles_storage module:', staticfiles_storage.__class__.__module__)

# Try to see if it's a lazy object
print('type:', type(staticfiles_storage))

# Force evaluation if lazy
if hasattr(staticfiles_storage, '_wrapped'):
    print('Wrapped:', staticfiles_storage._wrapped)
if hasattr(staticfiles_storage, '_setup'):
    staticfiles_storage._setup()
    print('After setup:', staticfiles_storage.__class__.__name__)

# Try url
url = staticfiles_storage.url('images/portfolio-preview.jpg')
print('URL:', url)

# Check if manifest exists
import os
manifest_path = os.path.join(settings.STATIC_ROOT, 'staticfiles.json')
print('STATIC_ROOT:', settings.STATIC_ROOT)
print('manifest exists at:', os.path.exists(manifest_path))
