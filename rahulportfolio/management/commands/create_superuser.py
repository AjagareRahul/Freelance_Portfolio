"""
Management command to create a superuser from environment variables.

This command creates a Django superuser only if:
1. The required environment variables are set
2. A superuser with that username doesn't already exist

Usage:
    python manage.py create_superuser

Required Environment Variables:
    DJANGO_SUPERUSER_USERNAME - Username for the superuser
    DJANGO_SUPERUSER_EMAIL - Email for the superuser
    DJANGO_SUPERUSER_PASSWORD - Password for the superuser

This is designed for deployment platforms like Render where shell access
is not available to run createsuperuser interactively.
"""

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = 'Creates a superuser from environment variables'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force recreate the superuser (delete existing and create new)',
        )

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Get credentials from environment variables
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        # Check if all required environment variables are set
        if not all([username, email, password]):
            missing = []
            if not username:
                missing.append('DJANGO_SUPERUSER_USERNAME')
            if not email:
                missing.append('DJANGO_SUPERUSER_EMAIL')
            if not password:
                missing.append('DJANGO_SUPERUSER_PASSWORD')
            
            self.stdout.write(self.style.WARNING(
                f'Superuser creation skipped. Missing environment variables: {", ".join(missing)}'
            ))
            self.stdout.write(self.style.WARNING(
                'Set these environment variables to create a superuser automatically.'
            ))
            return

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            if options['force']:
                self.stdout.write(f'Deleting existing superuser: {username}')
                User.objects.filter(username=username).delete()
            else:
                self.stdout.write(self.style.SUCCESS(
                    f'Superuser "{username}" already exists. Skipping creation.'
                ))
                return

        # Create the superuser
        try:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created superuser: {username}'
            ))
        except Exception as e:
            raise CommandError(f'Error creating superuser: {e}')
