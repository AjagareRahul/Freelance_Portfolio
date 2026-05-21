import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import SiteInfo
si = SiteInfo.objects.first()
print('Resume storage:', si.resume.storage)
print('Profile image storage:', si.profile_image.storage)
print('Resume URL:', si.resume.url)
print('Profile image URL:', si.profile_image.url)