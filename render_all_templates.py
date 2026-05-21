import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from django.test import RequestFactory
from django.template.loader import render_to_string
from portfolio.views import HomeView, AboutView, ProjectsView, ContactView, GalleryView

rf = RequestFactory()
request = rf.get('/')
request.session = {}

errors = []
templates = [
    ('home.html', HomeView.as_view()),
    ('about.html', AboutView.as_view()),
    ('projects.html', ProjectsView.as_view()),
    ('contact.html', ContactView.as_view()),
    ('gallery.html', GalleryView.as_view()),
]

for template_name, view_func in templates:
    try:
        if hasattr(view_func, 'as_view'):
            view = view_func.as_view()
            response = view(request)
            # Render the template with context
            if hasattr(response, 'context_data'):
                context = response.context_data
            else:
                # For TemplateResponse, render it
                response.render()
                context = response.context_data
            html = render_to_string(template_name, context, request=request)
            print(f'✓ {template_name}: rendered OK, size={len(html)}')
        else:
            # function view
            response = view_func(request)
            if hasattr(response, 'render'):
                response.render()
            html = response.content.decode()
            print(f'✓ {template_name}: rendered OK, size={len(html)}')
    except Exception as e:
        print(f'✗ {template_name}: ERROR - {e}')
        errors.append(template_name)

print(f'\nTotal errors: {len(errors)}')
if errors:
    print('Failed templates:', errors)
