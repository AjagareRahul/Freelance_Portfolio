import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import SiteInfo
si = SiteInfo.objects.first()
if si:
    print('SiteInfo profile_image:', si.profile_image.name if si.profile_image else None)
    print('SiteInfo resume:', si.resume.name if si.resume else None)
else:
    print('No SiteInfo')
