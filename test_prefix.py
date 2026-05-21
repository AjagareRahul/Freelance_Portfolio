import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import Project, Gallery, UpcomingProject, SiteInfo, Testimonial, BlogPost
from cloudinary_storage.storage import MediaCloudinaryStorage
import cloudinary

cloudinary.config(
    cloud_name='dfgp33gvs',
    api_key='159678591454118',
    api_secret='FtCj8RZ4MNe8iwblAfkuCK3XoZw',
    secure=True
)
storage = MediaCloudinaryStorage()

# Test: what URL does storage generate for a public_id without media/ prefix?
test_name = 'projects/test'
url = storage.url(test_name)
print('URL for "projects/test":', url)

test_name2 = 'media/projects/test'
url2 = storage.url(test_name2)
print('URL for "media/projects/test":', url2)

# Check PREFIX used by storage
from cloudinary_storage import app_settings
print('PREFIX:', app_settings.PREFIX)
