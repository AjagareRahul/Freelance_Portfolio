import os
import sys

sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')

import django
django.setup()

# Test imports
try:
    from portfolio.views import HomeView
    print('HomeView imported successfully')
    view = HomeView()
    print('HomeView instantiated')
    context = view.get_context_data()
    print('Context keys:', list(context.keys()))
    print('upcoming_projects:', context.get('upcoming_projects'))
except Exception as e:
    print('Error:', e)
    import traceback
    traceback.print_exc()
