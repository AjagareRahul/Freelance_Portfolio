"""
Management command to migrate local image files to Cloudinary.
Place original images in the same relative paths under a 'local_media' folder,
or ensure they exist under MEDIA_ROOT.

Usage: python manage.py migrate_to_cloudinary
Or: python upload_missing_images.py (if run manually)

This will:
- Find all ImageField/FileField values in Project, Gallery, UpcomingProject, SiteInfo, Testimonial, BlogPost
- For each that points to a local file that exists, upload to Cloudinary and update DB with new public_id
- Skip if file missing (needs manual upload)
"""

import os
import sys

# Setup Django
sys.path.insert(0, r'D:\Freelance_Portfolio')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rahulportfolio.settings')
import django
django.setup()

import cloudinary
import cloudinary.uploader
from django.conf import settings
from portfolio.models import Project, Gallery, UpcomingProject, SiteInfo, Testimonial, BlogPost
from cloudinary_storage.storage import MediaCloudinaryStorage

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
    secure=True
)

storage = MediaCloudinaryStorage()
MEDIA_ROOT = settings.MEDIA_ROOT

def upload_instance(instance, field_name):
    field = getattr(instance, field_name)
    if not field:
        return False
    name = field.name  # e.g., 'projects/rawmaterailimg.png'
    # If already a Cloudinary public_id (contains 'media/'), skip
    if name.startswith('media/'):
        print(f'  Already Cloudinary: {name}')
        return False

    full_path = os.path.join(MEDIA_ROOT, name)
    if not os.path.exists(full_path):
        print(f'  File missing locally: {full_path}')
        return False

    print(f'  Uploading {name}...')
    with open(full_path, 'rb') as f:
        from django.core.files.base import ContentFile
        content = ContentFile(f.read())
        # Use storage's save which returns public_id
        new_name = storage.save(name, content)
    # Update field
    setattr(instance, field_name, new_name)
    instance.save(update_fields=[field_name])
    print(f'  -> stored as {new_name}')
    return True

print('=== Migrating images to Cloudinary ===\n')

print('Projects:')
for p in Project.objects.all():
    print(f'  {p.title}: {p.image.name}')
    upload_instance(p, 'image')

print('\nGallery:')
for g in Gallery.objects.all():
    print(f'  {g.title}: {g.image.name}')
    upload_instance(g, 'image')

print('\nUpcoming Projects:')
for u in UpcomingProject.objects.all():
    print(f'  {u.title}: {u.image.name}')
    upload_instance(u, 'image')

print('\nSiteInfo:')
si = SiteInfo.objects.first()
if si:
    print(f'  SiteInfo: profile={si.profile_image.name}, resume={si.resume.name if si.resume else None}')
    upload_instance(si, 'profile_image')
    upload_instance(si, 'resume')

print('\nTestimonials:')
for t in Testimonial.objects.all():
    print(f'  {t.client_name}: {t.client_image.name if t.client_image else None}')
    upload_instance(t, 'client_image')

print('\nBlogPosts:')
for b in BlogPost.objects.all():
    print(f'  {b.title}: {b.image.name if b.image else None}')
    upload_instance(b, 'image')

print('\nDone.')
