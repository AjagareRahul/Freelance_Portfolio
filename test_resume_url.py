import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import SiteInfo
si = SiteInfo.objects.first()
print('Resume field name:', si.resume.name)
print('Resume field url:', si.resume.url)
print('Resume field storage:', si.resume.field.storage.__class__.__name__)

# Also check with storage.url directly
from cloudinary_storage.storage import MediaCloudinaryStorage
storage = MediaCloudinaryStorage()
url = storage.url(si.resume.name)
print('Direct storage.url:', url)

# Check if adding .pdf changes existence:
url_with_pdf = url + '.pdf'
print('Test with .pdf extension:', url_with_pdf)

# Check existence via HEAD request
import requests
try:
    r = requests.head(url, timeout=10)
    print('HEAD', url, '->', r.status_code)
except Exception as e:
    print('Error', e)

try:
    r2 = requests.head(url_with_pdf, timeout=10)
    print('HEAD with .pdf', url_with_pdf, '->', r2.status_code)
except Exception as e:
    print('Error', e)
