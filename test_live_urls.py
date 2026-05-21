import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import SiteInfo
si = SiteInfo.objects.first()
print('Resume URL:', si.resume.url)
print('Profile image URL:', si.profile_image.url)

# Try to open the URL
import requests
try:
    r = requests.get(si.resume.url, timeout=10)
    print('Resume HTTP status:', r.status_code)
except Exception as e:
    print('Resume fetch error:', e)

try:
    r2 = requests.get(si.profile_image.url, timeout=10)
    print('Profile image HTTP status:', r2.status_code)
except Exception as e:
    print('Profile image fetch error:', e)
