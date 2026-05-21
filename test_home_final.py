import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ['DEBUG'] = 'False'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from django.test import RequestFactory
from django.template.loader import render_to_string
from portfolio.views import HomeView

# Temporarily override staticfiles_storage to avoid manifest errors in local env
from django.contrib.staticfiles.storage import StaticFilesStorage
from django.conf import settings
settings.STORAGES['staticfiles']['BACKEND'] = 'django.contrib.staticfiles.storage.StaticFilesStorage'

rf = RequestFactory()
request = rf.get('/')
request.session = {}
view = HomeView.as_view()(request)
context = view.context_data

try:
    html = render_to_string('portfolio/home.html', context, request=request)
    print('Home rendered OK, length', len(html))
    # Check for presence of some expected content
    if 'Upcoming Projects' in html:
        print('Upcoming Projects section present')
    if 'resume' in html or '/media/' in html:
        print('Resume link present')
except Exception as e:
    print('ERROR:', e)
    import traceback
    traceback.print_exc()