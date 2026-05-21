import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from django.test import Client
c = Client()
resp = c.get('/')
print('Status:', resp.status_code)
if resp.status_code == 200:
    print('Home page renders OK')
    # Count upcoming projects section presence
    content = resp.content.decode()
    if 'Upcoming Projects' in content:
        print('Upcoming Projects section present')
    else:
        print('Upcoming Projects section missing')
else:
    print('Error:', resp.content[:500])
