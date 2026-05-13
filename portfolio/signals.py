# Signals for automatic Cloudinary file cleanup
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
import os

from .models import Project, Gallery, UpcomingProject, SiteInfo, Testimonial, BlogPost

def delete_file_from_storage(instance, field_name):
    """Delete file from storage backend (Cloudinary) if it exists"""
    field = getattr(instance, field_name)
    if field:
        # The storage backend's delete method will be called
        try:
            field.delete(save=False)
        except Exception as e:
            # Log but don't raise
            print(f"Failed to delete {field_name} for {instance}: {e}")

# Project signals
@receiver(pre_delete, sender=Project)
def delete_project_image(sender, instance, **kwargs):
    delete_file_from_storage(instance, 'image')

@receiver(pre_save, sender=Project)
def delete_old_project_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old = Project.objects.get(pk=instance.pk)
    except Project.DoesNotExist:
        return
    if old.image and old.image != instance.image:
        delete_file_from_storage(old, 'image')

# Gallery signals
@receiver(pre_delete, sender=Gallery)
def delete_gallery_image(sender, instance, **kwargs):
    delete_file_from_storage(instance, 'image')

@receiver(pre_save, sender=Gallery)
def delete_old_gallery_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old = Gallery.objects.get(pk=instance.pk)
    except Gallery.DoesNotExist:
        return
    if old.image and old.image != instance.image:
        delete_file_from_storage(old, 'image')

# UpcomingProject signals
@receiver(pre_delete, sender=UpcomingProject)
def delete_upcoming_image(sender, instance, **kwargs):
    delete_file_from_storage(instance, 'image')

@receiver(pre_save, sender=UpcomingProject)
def delete_old_upcoming_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old = UpcomingProject.objects.get(pk=instance.pk)
    except UpcomingProject.DoesNotExist:
        return
    if old.image and old.image != instance.image:
        delete_file_from_storage(old, 'image')

# SiteInfo signals (profile_image, resume)
@receiver(pre_delete, sender=SiteInfo)
def delete_siteinfo_files(sender, instance, **kwargs):
    delete_file_from_storage(instance, 'profile_image')
    delete_file_from_storage(instance, 'resume')

@receiver(pre_save, sender=SiteInfo)
def delete_old_siteinfo_files_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old = SiteInfo.objects.get(pk=instance.pk)
    except SiteInfo.DoesNotExist:
        return
    if old.profile_image and old.profile_image != instance.profile_image:
        delete_file_from_storage(old, 'profile_image')
    if old.resume and old.resume != instance.resume:
        delete_file_from_storage(old, 'resume')

# Testimonial signals (client_image)
@receiver(pre_delete, sender=Testimonial)
def delete_testimonial_image(sender, instance, **kwargs):
    delete_file_from_storage(instance, 'client_image')

@receiver(pre_save, sender=Testimonial)
def delete_old_testimonial_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old = Testimonial.objects.get(pk=instance.pk)
    except Testimonial.DoesNotExist:
        return
    if old.client_image and old.client_image != instance.client_image:
        delete_file_from_storage(old, 'client_image')

# BlogPost signals (image)
@receiver(pre_delete, sender=BlogPost)
def delete_blogpost_image(sender, instance, **kwargs):
    delete_file_from_storage(instance, 'image')

@receiver(pre_save, sender=BlogPost)
def delete_old_blogpost_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        old = BlogPost.objects.get(pk=instance.pk)
    except BlogPost.DoesNotExist:
        return
    if old.image and old.image != instance.image:
        delete_file_from_storage(old, 'image')
