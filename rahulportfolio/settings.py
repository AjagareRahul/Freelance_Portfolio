"""
Django settings for rahulportfolio project.
Production-ready configuration for Render deployment.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(os.path.join(BASE_DIR, '.env'))

# =============================================================================
# SECRET KEY - Load from environment variable (REQUIRED for production)
# =============================================================================
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-development-key-change-in-production')

# =============================================================================
# DEBUG MODE - Production auto-detection
# =============================================================================
# SECURITY WARNING: don't run with debug turned on in production!
# If DEBUG env var is explicitly set, use it; otherwise auto-detect:
#   - Render/Heroku: DEBUG=False by default
#   - Local dev: DEBUG=True by default
DEBUG_ENV = os.environ.get('DEBUG')
if DEBUG_ENV is not None:
    DEBUG = DEBUG_ENV.lower() == 'true'
else:
    # Auto-detect: if running on Render/Heroku (DATABASE_URL present), disable debug
    DEBUG = not bool(os.environ.get('RENDER_EXTERNAL_HOSTNAME') or os.environ.get('DATABASE_URL'))

# =============================================================================
# ALLOWED_HOSTS & CSRF - Production domains
# =============================================================================
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS = [RENDER_EXTERNAL_HOSTNAME, 'localhost', '127.0.0.1']
    # Trusted origins for CSRF when behind proxy
    CSRF_TRUSTED_ORIGINS = [f'https://{RENDER_EXTERNAL_HOSTNAME}', f'http://{RENDER_EXTERNAL_HOSTNAME}']
else:
    allowed_hosts_env = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1')
    ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_env.split(',') if host.strip()]
    CSRF_TRUSTED_ORIGINS = []

# =============================================================================
# Application definition
# =============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Third party apps
    'cloudinary',
    'cloudinary_storage',
    # Local apps
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static file serving
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Custom middleware
    'rahulportfolio.middleware.VisitorCountMiddleware',
    'rahulportfolio.middleware.LastVisitMiddleware',
]

ROOT_URLCONF = 'rahulportfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Custom context processors
                'rahulportfolio.context_processors.site_info',
                'rahulportfolio.context_processors.social_links',
                'rahulportfolio.context_processors.visitor_count',
                'rahulportfolio.context_processors.featured_skills',
                'rahulportfolio.context_processors.recent_projects',
            ],
            'libraries': {
                'portfolio_tags': 'portfolio.templatetags.portfolio_tags',
            },
        },
    },
]

WSGI_APPLICATION = 'rahulportfolio.wsgi.application'

# =============================================================================
# Database configuration for production (PostgreSQL on Render)
# =============================================================================
import dj_database_url

# Primary database configuration - supports both PostgreSQL and SQLite
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # Production/PostgreSQL - Parse DATABASE_URL (Render, Heroku, etc.)
    try:
        DATABASES = {
            'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
        }
    except Exception as e:
        # If parsing fails, log warning and fallback to SQLite
        import warnings
        warnings.warn(f"Failed to parse DATABASE_URL: {e}. Falling back to SQLite.", RuntimeWarning)
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
else:
    # Development - SQLite fallback (faster, no external dependency)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    
    # Alternative: Uncomment below to use PostgreSQL locally without DATABASE_URL
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': 'rahulportfolio',
    #         'USER': 'postgres',
    #         'PASSWORD': 'your_password',
    #         'HOST': 'localhost',
    #         'PORT': '5432',
    #     }
    # }

# =============================================================================
# Password validation
# =============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# =============================================================================
# Internationalization
# =============================================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# =============================================================================
# Static files (CSS, JavaScript, Images)
# =============================================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# WhiteNoise configuration for serving static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =============================================================================
# Cloudinary Configuration (for media and static file storage)
# =============================================================================
import warnings

# Try importing Cloudinary SDK (optional - graceful degradation if missing)
try:
    import cloudinary
    import cloudinary.uploader
    import cloudinary.api
    CLOUDINARY_SDK_AVAILABLE = True
except ImportError:
    CLOUDINARY_SDK_AVAILABLE = False
    warnings.warn("Cloudinary SDK not installed. Install 'cloudinary' and 'django-cloudinary-storage' for CDN media storage.", RuntimeWarning)

# Cloudinary credentials from environment variables
CLOUDINARY_CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME', '')
CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY', '')
CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET', '')

# Cloudinary storage configuration
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': CLOUDINARY_CLOUD_NAME,
    'API_KEY': CLOUDINARY_API_KEY,
    'API_SECRET': CLOUDINARY_API_SECRET,
    'SECURE': True,  # Always use HTTPS
}

# Configure Cloudinary SDK if all credentials are available and SDK imported
if CLOUDINARY_SDK_AVAILABLE and CLOUDINARY_CLOUD_NAME and CLOUDINARY_API_KEY and CLOUDINARY_API_SECRET:
    cloudinary.config(
        cloud_name=CLOUDINARY_CLOUD_NAME,
        api_key=CLOUDINARY_API_KEY,
        api_secret=CLOUDINARY_API_SECRET,
        secure=True
    )
    # Production: Use Cloudinary CDN for all media files (images, videos, documents)
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    
    # Optional: Serve static files via Cloudinary CDN (uncomment to enable)
    # CLOUDINARY_STATICFILES = os.environ.get('CLOUDINARY_STATICFILES', '').lower() == 'true'
    # if CLOUDINARY_STATICFILES:
    #     STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticCloudinaryStorage'
else:
    # Development fallback: use local filesystem storage
    if DEBUG:
        pass  # Local development uses default FileSystemStorage
    else:
        # Production without Cloudinary - CRITICAL WARNING
        warnings.warn(
            "\n" + "="*70 + "\n"
            "⚠️  CLOUDINARY NOT CONFIGURED - MEDIA UPLOADS WILL FAIL ⚠️\n"
            "="*70 + "\n"
            "Set environment variables:\n"
            "  CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET\n"
            "Get credentials from: https://cloudinary.com/console\n"
            "="*70,
            RuntimeWarning
        )

# Media URL configuration (works with Cloudinary)
MEDIA_URL = '/media/'


# =============================================================================
# Authentication settings
# =============================================================================

LOGIN_URL = 'portfolio:login'
LOGIN_REDIRECT_URL = 'portfolio:dashboard'
LOGOUT_REDIRECT_URL = 'portfolio:home'

# =============================================================================
# Session settings
# =============================================================================

SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 1 week
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# =============================================================================
# Security Settings - Production hardened
# =============================================================================

# Clickjacking protection (always enabled)
X_FRAME_OPTIONS = 'DENY'

# Auto-enable security features in production (when not DEBUG)
if not DEBUG:
    # Force HTTPS/SSL in production (Render provides SSL)
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
    # HSTS (HTTP Strict Transport Security) - 1 year
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    
    # Secure cookies in production
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # Prevent content type sniffing
    SECURE_CONTENT_TYPE_NOSNIFF = True
    
    # CSRF trusted origins for Render domain
    if RENDER_EXTERNAL_HOSTNAME:
        CSRF_TRUSTED_ORIGINS = [
            f'https://{RENDER_EXTERNAL_HOSTNAME}',
            f'http://{RENDER_EXTERNAL_HOSTNAME}'
        ]
else:
    # Development: disable strict security
    SECURE_SSL_REDIRECT = False
    SECURE_PROXY_SSL_HEADER = None
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_CONTENT_TYPE_NOSNIFF = False
    CSRF_TRUSTED_ORIGINS = []
# SECURITY SETTINGS FOR PRODUCTION (Required by check --deploy)
# =============================================================================

# Only enable security settings in production (when DEBUG=False)
if not DEBUG:
    # Force HTTPS/SSL in production
    SECURE_SSL_REDIRECT = True
    
    # HSTS (HTTP Strict Transport Security) - 1 year for production
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    
    # Secure cookies in production
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # Prevent content type sniffing in production
    SECURE_CONTENT_TYPE_NOSNIFF = True
else:
    # Force HTTPS/SSL - Disabled for local development
    SECURE_SSL_REDIRECT = False

    # HSTS (HTTP Strict Transport Security) - Disabled for local development
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False

    # Secure cookies - Disabled for local development
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

    # Prevent content type sniffing - Disabled for local development
    SECURE_CONTENT_TYPE_NOSNIFF = False

# =============================================================================
# Security Settings - Production hardened
# =============================================================================

# Auto-enable security features in production (when not DEBUG)
if not DEBUG:
    # Force HTTPS/SSL in production (Render provides SSL)
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    
    # HSTS (HTTP Strict Transport Security) - 1 year
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    
    # Secure cookies in production
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    
    # Prevent content type sniffing
    SECURE_CONTENT_TYPE_NOSNIFF = True
    
    # CSRF trusted origins for Render domain
    if RENDER_EXTERNAL_HOSTNAME:
        CSRF_TRUSTED_ORIGINS = [
            f'https://{RENDER_EXTERNAL_HOSTNAME}',
            f'http://{RENDER_EXTERNAL_HOSTNAME}'
        ]
else:
    # Development: disable strict security
    SECURE_SSL_REDIRECT = False
    SECURE_PROXY_SSL_HEADER = None
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_CONTENT_TYPE_NOSNIFF = False
    CSRF_TRUSTED_ORIGINS = []

# =============================================================================
# Admin panel configuration
# =============================================================================

# Django admin panel site header
ADMIN_SITE_HEADER = "Rahul's Portfolio Admin"
ADMIN_SITE_TITLE = "Portfolio Admin"
ADMIN_INDEX_TITLE = "Welcome to Portfolio Admin"

# =============================================================================
# Logging configuration for production
# =============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
