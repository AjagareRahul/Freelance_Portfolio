# Render Deployment Configuration

## Environment Variables to Set on Render

Go to your Render dashboard → Service → Environment tab and set:

### Required Variables

```
# Django Settings
SECRET_KEY=<generate-a-secure-random-key>
DEBUG=False
ALLOWED_HOSTS=freelance-portfolio-53d0.onrender.com

# Database (PostgreSQL - Render provides this automatically)
# Render will set DATABASE_URL automatically when you add a PostgreSQL instance
# Format: postgres://user:password@host:port/database

# Cloudinary (Media Storage)
CLOUDINARY_CLOUD_NAME=Root
CLOUDINARY_API_KEY=159678591454118
CLOUDINARY_API_SECRET=FtCj8RZ4MNe8iwblAfkuCK3XoZw

# Render Detection (auto-set by Render, but ensure it's present)
RENDER_EXTERNAL_HOSTNAME=freelance-portfolio-53d0.onrender.com
```

**Generate SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Common Issues & Fixes

### Issue 1: Site shows "Application Error"
**Cause:** Missing database migrations or Cloudinary not configured.

**Fix:**
1. Check Render logs: `View Logs` button on Render dashboard
2. Common errors:
   - `django.core.exceptions.ImproperlyConfigured: SECRET_KEY` → Set SECRET_KEY
   - Database connection error → Verify DATABASE_URL is set
   - Cloudinary import error → Ensure `cloudinary` and `django-cloudinary-storage` in requirements.txt

### Issue 2: Static files not loading (CSS/JS broken)
**Cause:** WhiteNoise not configured or collectstatic not run.

**Fix:**
The Procfile runs gunicorn, but collectstatic must run on deploy.

Render runs `collectstatic` automatically if:
- `DISABLE_COLLECTSTATIC=1` is NOT set
- You have a `requirements.txt` with `whitenoise`

**Manual fix:** In Render service settings, uncheck "Disable Collect Static"

### Issue 3: Media uploads fail (403/404 on images)
**Cause:** Cloudinary credentials missing or not set as environment variables.

**Fix:**
1. Verify ALL three Cloudinary env vars are set exactly:
   - `CLOUDINARY_CLOUD_NAME=Root`
   - `CLOUDINARY_API_KEY=159678591454118`
   - `CLOUDINARY_API_SECRET=FtCj8RZ4MNe8iwblAfkuCK3XoZw`
2. Redeploy service after setting env vars

### Issue 4: Database tables missing
**Cause:** Migrations not applied.

**Fix:**
Run in Render Shell (Dashboard → Shell):
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

Or add a `postdeploy` script in Render:

**render.yaml** (if using Blueprint):
```yaml
services:
  - type: web
    name: freelance-portfolio
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn rahulportfolio.wsgi --log-file -
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: your-db-name
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: false
    postDeployCommand: python manage.py migrate && python manage.py collectstatic --noinput
```

### Issue 5: ALLOWED_HOSTS error
**Cause:** Domain not in ALLOWED_HOSTS.

**Fix:** Set in Render env vars:
```
ALLOWED_HOSTS=freelance-portfolio-53d0.onrender.com
```

Note: Your current settings.py auto-detects Render and adds the domain automatically via `RENDER_EXTERNAL_HOSTNAME`. But explicit `ALLOWED_HOSTS` is safer.

### Issue 6: CSRF/CSRF_TRUSTED_ORIGINS missing
If you get CSRF errors, add:
```
CSRF_TRUSTED_ORIGINS=https://freelance-portfolio-53d0.onrender.com
```

Add to `settings.py` (already partially there):
```python
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',') if os.environ.get('CSRF_TRUSTED_ORIGINS') else []
```

## Quick Diagnostic Checklist

- [ ] All environment variables set in Render dashboard
- [ ] `collectstatic` ran successfully (check build logs)
- [ ] Database migrations applied (`python manage.py migrate`)
- [ ] `DEBUG=False` (production)
- [ ] `SECRET_KEY` set (not the dev default)
- [ ] Cloudinary credentials all 3 set
- [ ] `ALLOWED_HOSTS` includes your Render domain
- [ ] No import errors in logs

## Monitor Logs

1. Go to Render dashboard
2. Click your service
3. Click **Logs** tab
4. Look for `ERROR` or `Traceback`
5. Common startup errors appear within first 30 seconds

## Need Help?

Check your logs first:
```
[render logs output]
```

Most common fix: Set `SECRET_KEY` and run migrations.
