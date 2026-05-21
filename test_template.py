import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

from django.test import RequestFactory
from portfolio.views import HomeView
from django.template import Template, Context

rf = RequestFactory()
request = rf.get('/')
view = HomeView()
request.session = {}  # dummy
view.request = request

try:
    context = view.get_context_data()
    print('Context built successfully')
    print('upcoming_projects type:', type(context['upcoming_projects']))
    print('upcoming_projects count:', context['upcoming_projects'].count())
    
    # Render template
    from django.template.loader import render_to_string
    html = render_to_string('portfolio/home.html', context, request=request)
    print('Template rendered successfully, length:', len(html))
    # Check if upcoming section appears
    if 'Upcoming Projects' in html:
        print('Upcoming Projects section found in rendered HTML')
    else:
        print('WARNING: Upcoming Projects section NOT in HTML')
        # Show snippet around where it should be
        idx = html.find('<!-- Testimonials -->')
        print('Snippet:', html[max(0, idx-200):idx+200])
except Exception as e:
    print('Error:', e)
    import traceback
    traceback.print_exc()
