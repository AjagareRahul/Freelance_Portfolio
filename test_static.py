import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from django.templatetags.static import static
try:
    url = static('images/portfolio-preview.jpg')
    print('Static URL:', url)
except Exception as e:
    print('Error:', e)
    import traceback
    traceback.print_exc()
