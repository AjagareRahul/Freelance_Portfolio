import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import SiteInfo
si = SiteInfo.objects.first()
if si:
    print('SiteInfo:')
    print('  profile_image:', si.profile_image)
    print('  profile_image.name:', si.profile_image.name if si.profile_image else None)
    print('  resume:', si.resume)
    print('  resume.name:', si.resume.name if si.resume else None)
    if si.resume:
        try:
            print('  resume.url:', si.resume.url)
        except Exception as e:
            print('  resume.url ERROR:', e)
