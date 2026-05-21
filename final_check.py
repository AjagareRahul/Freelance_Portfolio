import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from django.conf import settings
from django.core.files.storage import default_storage
from portfolio.models import SiteInfo

print('=== Final Verification ===')
print('DEFAULT_FILE_STORAGE:', settings.DEFAULT_FILE_STORAGE)
print('STORAGES:', settings.STORAGES)
print('default_storage class:', default_storage.__class__.__name__)

si = SiteInfo.objects.first()
if si and si.resume:
    print('Resume URL:', si.resume.url)
    # Verify it matches Cloudinary pattern
    if 'res.cloudinary.com' in si.resume.url:
        print('✓ Resume serves from Cloudinary')
    else:
        print('✗ Resume NOT from Cloudinary')

# Check a project image
from portfolio.models import Project
p = Project.objects.first()
if p and p.image:
    print('Project image URL:', p.image.url)
    if 'res.cloudinary.com' in p.image.url:
        print('✓ Project image URL is Cloudinary')
    else:
        print('✗ Project image NOT from Cloudinary (file may not exist yet)')
