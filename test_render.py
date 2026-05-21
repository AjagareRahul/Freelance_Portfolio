import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

from django.conf import settings
print('DEBUG:', settings.DEBUG)
print('STATICFILES_STORAGE:', settings.STATICFILES_STORAGE)
print('DEFAULT_FILE_STORAGE:', settings.DEFAULT_FILE_STORAGE)

from django.template.loader import render_to_string
from portfolio.views import HomeView
from django.test import RequestFactory

rf = RequestFactory()
request = rf.get('/')
view = HomeView()
request.session = {}
view.request = request

context = view.get_context_data()
try:
    html = render_to_string('portfolio/home.html', context, request=request)
    print('Template rendered OK, length:', len(html))
    if 'Upcoming Projects' in html:
        print('Upcoming Projects section present')
    else:
        print('Upcoming Projects section MISSING')
except Exception as e:
    print('Render error:', e)
    import traceback
    traceback.print_exc()
