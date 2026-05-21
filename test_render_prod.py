import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ['DEBUG'] = 'False'  # Force DEBUG=False
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from django.conf import settings
print('DEBUG:', settings.DEBUG)
print('STATICFILES_STORAGE:', settings.STATICFILES_STORAGE)

from django.template.loader import render_to_string
from django.test import RequestFactory
from portfolio.views import HomeView

rf = RequestFactory()
request = rf.get('/')
request.session = {}
view = HomeView.as_view()(request)
context = view.context_data
try:
    html = render_to_string('portfolio/home.html', context, request=request)
    print('Rendered successfully, length:', len(html))
    if 'portfolio-preview' in html:
        print('Preview image referenced')
except Exception as e:
    print('Render error:', e)
