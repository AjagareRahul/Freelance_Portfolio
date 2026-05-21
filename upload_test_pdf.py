import os, sys
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

from portfolio.models import SiteInfo
from django.core.files.base import ContentFile
from io import BytesIO

# Create a simple PDF in memory
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

buffer = BytesIO()
p = canvas.Canvas(buffer, pagesize=letter)
p.drawString(100, 750, "Test PDF")
p.showPage()
p.save()
buffer.seek(0)
content = ContentFile(buffer.read(), name='test.pdf')

si = SiteInfo.objects.first()
si.resume.save('test_resume.pdf', content, save=True)
print('Saved resume PDF')
print('Name:', si.resume.name)
print('URL:', si.resume.url)

# Check existence
from django.core.files.storage import default_storage
print('Exists?', default_storage.exists(si.resume.name))
