import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ['DEBUG'] = 'False'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from django.test import RequestFactory
from django.template.loader import render_to_string
from portfolio.views import HomeView

rf = RequestFactory()
request = rf.get('/')
request.session = {}
view = HomeView.as_view()(request)
context = view.context_data
try:
    html = render_to_string('portfolio/home.html', context, request=request)
    print('Rendered home OK, length', len(html))
except Exception as e:
    print('Render error:', e)
    import traceback
    traceback.print_exc()