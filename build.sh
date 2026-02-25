#!/usr/bin/env bash
# Build script for deployment (e.g., Render)
set -e

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations
python manage.py migrate --noinput

# Create superuser from environment variables (if provided)
# This command is idempotent - it won't create duplicates
python manage.py create_superuser
