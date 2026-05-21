# Check if cloudinary_storage has delete-on-delete signal built-in
# Look at the installed apps and see if it's registered
import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from django.conf import settings
print('INSTALLED_APPS:')
for app in settings.INSTALLED_APPS:
    if 'cloudinary' in app.lower():
        print(' ', app)

# Also check if signals are connected in the package
import cloudinary_storage.signals as sig
print('\ncloudinary_storage.signals module:', sig)
print('Attributes:', dir(sig))

# Check if any signal receivers are registered
from django.db.models.signals import post_delete, pre_save
print('\nChecking for connected signals...')
# Inspect post_delete receivers
from django.dispatch import receiver
print('post_delete receivers:', len(post_delete.receivers))
for r in post_delete.receivers:
    print(' ', r)
