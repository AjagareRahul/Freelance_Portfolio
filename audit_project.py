"""
Comprehensive project audit checklist:
- Settings issues
- URL configuration
- Model issues
- View issues
- Template issues
- Static files
- Middleware
- Signals
- Forms
- Admin
"""

import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from django.conf import settings

print('=== SETTINGS CHECK ===')
issues = []

# Check critical settings
checks = [
    ('DEBUG', settings.DEBUG),
    ('SECRET_KEY set', bool(settings.SECRET_KEY and settings.SECRET_KEY != '')),
    ('ALLOWED_HOSTS', bool(settings.ALLOWED_HOSTS)),
    ('INSTALLED_APPS', 'cloudinary' in settings.INSTALLED_APPS),
    ('INSTALLED_APPS', 'cloudinary_storage' in settings.INSTALLED_APPS),
    ('STORAGES set', hasattr(settings, 'STORAGES')),
    ('DEFAULT_FILE_STORAGE', 'cloudinary_storage' in settings.DEFAULT_FILE_STORAGE),
    ('STATIC_URL', settings.STATIC_URL),
    ('MEDIA_URL', settings.MEDIA_URL),
    ('DATABASES configured', bool(settings.DATABASES.get('default'))),
    ('TEMPLATES DIRS', bool(settings.TEMPLATES[0]['DIRS'])),
]

for name, passed in checks:
    status = '✓' if passed else '✗'
    print(f'  {status} {name}: {passed}')

print('\n=== MODEL CHECK ===')
from portfolio.models import Project, Gallery, UpcomingProject, SiteInfo, Testimonial, BlogPost
models = [Project, Gallery, UpcomingProject, SiteInfo, Testimonial, BlogPost]
for m in models:
    # Check image fields exist
    image_fields = [f for f in m._meta.fields if f.__class__.__name__ in ('ImageField', 'FileField')]
    print(f'  {m.__name__}: image fields = {[f.name for f in image_fields]}')

print('\n=== VIEW CHECK ===')
# Import all views to catch syntax errors
from portfolio import views
view_classes = [v for v in dir(views) if v.endswith('View') or v.endswith('view')]
print(f'  Found {len(view_classes)} view functions/classes')

print('\n=== URL CHECK ===')
from django.urls import reverse, NoReverseMatch
url_errors = []
# Test some critical URLs
test_urls = [
    'portfolio:home',
    'portfolio:about',
    'portfolio:projects',
    'portfolio:contact',
    'portfolio:login',
    'portfolio:register',
]
for name in test_urls:
    try:
        url = reverse(name)
        print(f'  ✓ {name}: {url}')
    except NoReverseMatch as e:
        print(f'  ✗ {name}: {e}')
        url_errors.append(name)

print('\n=== TEMPLATE CHECK ===')
from django.template.loader import get_template
templates_to_check = [
    'base.html',
    'portfolio/home.html',
    'portfolio/about.html',
    'portfolio/projects.html',
    'portfolio/contact.html',
    'portfolio/gallery.html',
    'portfolio/dashboard.html',
]
for tpl in templates_to_check:
    try:
        t = get_template(tpl)
        print(f'  ✓ {tpl}')
    except Exception as e:
        print(f'  ✗ {tpl}: {e}')
        issues.append(tpl)

print('\n=== CLOUDINARY CONFIG ===')
from cloudinary_storage.storage import MediaCloudinaryStorage
from django.core.files.storage import default_storage
print(f'  default_storage: {default_storage.__class__.__name__}')
print(f'  MediaCloudinaryStorage: {MediaCloudinaryStorage}')
try:
    from cloudinary import config as cloudinary_config
    print(f'  Cloudinary cloud_name: {cloudinary_config().cloud_name}')
except Exception as e:
    print(f'  ✗ Cloudinary not configured: {e}')

print('\n=== SIGNALS CHECK ===')
# Check if signals module is imported in apps.py
try:
    import portfolio.signals
    print('  ✓ portfolio.signals module can be imported')
except ImportError as e:
    print(f'  ✗ Cannot import signals: {e}')
    issues.append('signals import')

print('\n=== SUMMARY ===')
print(f'Issues found: {len(issues)}')
if issues:
    print('Issues:', issues)
