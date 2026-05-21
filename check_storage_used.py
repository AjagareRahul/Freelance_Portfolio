import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import SiteInfo
si = SiteInfo.objects.first()
print('SiteInfo resume field storage:', si.resume.field.storage)
print('Storage class:', si.resume.field.storage.__class__.__name__)
print('Storage module:', si.resume.field.storage.__class__.__module__)

# Also default_storage
from django.core.files.storage import default_storage
print('default_storage:', default_storage.__class__.__name__)

# Check if they are same
print('Same?', si.resume.field.storage is default_storage)
