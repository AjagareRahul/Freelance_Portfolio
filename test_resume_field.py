import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import SiteInfo
si = SiteInfo.objects.first()
print('Resume field:', si.resume)
print('Resume storage type:', type(si.resume.field.storage).__name__)
try:
    url = si.resume.url
    print('Resume URL:', url)
except Exception as e:
    print('Error getting url:', e)
    import traceback
    traceback.print_exc()