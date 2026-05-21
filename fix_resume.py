import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import SiteInfo
from django.core.files import File

si = SiteInfo.objects.first()
print('Current resume storage:', si.resume.storage)
print('Current resume name:', si.resume.name)
print('Current resume url:', si.resume.url)

# Local path to the resume file (we know it's in media/resume/Rahul_Ajagare.pdf)
local_resume_path = r'D:\Freelance_Portfolio\media\resume\Rahul_Ajagare.pdf'
print('Local resume path:', local_resume_path)
print('Local resume exists:', os.path.exists(local_resume_path))

if os.path.exists(local_resume_path):
    # Open the file and save it again to trigger upload with current storage
    with open(local_resume_path, 'rb') as f:
        si.resume.save(os.path.basename(local_resume_path), File(f), save=True)
    print('After saving:')
    print('  Resume storage:', si.resume.storage)
    print('  Resume name:', si.resume.name)
    print('  Resume url:', si.resume.url)
else:
    print('Local resume file not found!')