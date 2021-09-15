# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GENERAL IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

import dj_database_url
import django_heroku
import os

from decouple import config
from pathlib import Path

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CELERY IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from celery.schedules import crontab


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CORE
# └─────────────────────────────────────────────────────────────────────────────────────

# Retrieve secret key from .env
SECRET_KEY = config("SECRET_KEY")

# Define base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Set URL configuration
ROOT_URLCONF = "config.urls"

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ ENVIRONMENT
# └─────────────────────────────────────────────────────────────────────────────────────

# Define environment constants
LOCAL = "local"
STAGING = "staging"
PRODUCTION = "production"

# Retrieve environment from .env
ENVIRONMENT = config("ENVIRONMENT", default=PRODUCTION)

# Retrieve debug from .env
DEBUG = config("DEBUG", cast=bool, default=False) and ENVIRONMENT != PRODUCTION

# Determine whether to enable Django Admin
ENABLE_DJANGO_ADMIN = config("ENABLE_DJANGO_ADMIN", cast=bool, default=True)

# Determine whether to enable browsable API
ENABLE_BROWSABLE_API = config(
    "ENABLE_BROWSABLE_API", cast=bool, default=ENVIRONMENT in [LOCAL, STAGING]
)

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ SERVER
# └─────────────────────────────────────────────────────────────────────────────────────

# Define allowed hosts
ALLOWED_HOSTS = [h.strip() for h in config("ALLOWED_HOSTS", default="").split(",")]

# Set WSGI configuration
WSGI_APPLICATION = "config.wsgi.application"

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ SECURITY
# └─────────────────────────────────────────────────────────────────────────────────────

# Allow any cross-origin requests
CORS_ALLOW_ALL_ORIGINS = True

# Check if staging or production
if ENVIRONMENT in [STAGING, PRODUCTION]:

    # Enforce https
    SECURE_SSL_REDIRECT = True

    # Enforce HTTP Strict Transport Security (1 year)
    SECURE_HSTS_SECONDS = 31536000

    # Configure https header (needed for Heroku)
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # Needed for Heroku

    # Enforce secure cookies
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ AUTHENTICATION
# └─────────────────────────────────────────────────────────────────────────────────────

# Set custom user model
AUTH_USER_MODEL = "user.User"

# Define password validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ INSTALLED APPS
# └─────────────────────────────────────────────────────────────────────────────────────

# Define installed apps
INSTALLED_APPS = [
    # Django Contrib
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Django Extensions
    "django_extensions",
    # Django Storages
    "storages",
    # Django REST Framework
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "dynamic_rest",
    # Django Celery Beat
    "django_celery_beat",
    # Project Apps
    "currency",
    "location",
    "user",
]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ MIDDLEWARE
# └─────────────────────────────────────────────────────────────────────────────────────

# Define middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TEMPLATES
# └─────────────────────────────────────────────────────────────────────────────────────

# Define template settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ LANGUAGE
# └─────────────────────────────────────────────────────────────────────────────────────

# Set language code to US English
LANGUAGE_CODE = "en-us"

# Disable Django's translation system
USE_I18N = False

# Disable localized formatting of numbers and dates
USE_L10N = False

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ TIMEZONE
# └─────────────────────────────────────────────────────────────────────────────────────

# Set timezone to UTC
TIME_ZONE = "UTC"

# Use timezone-aware datetimes
USE_TZ = True

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DATABASES
# └─────────────────────────────────────────────────────────────────────────────────────

# Get remote database URL
database_url = config("DATABASE_URL", "")

# Check if database URL is defined
if database_url:

    # Define lifetime of a database connection
    conn_max_age = config("DATABASE_CONN_MAX_AGE", cast=int, default=60)

    # Define databases
    DATABASES = {
        "default": dj_database_url.parse(
            database_url, conn_max_age=conn_max_age, ssl_require=True
        )
    }

# Handle case of local database
else:

    # Get database credentials
    database_engine = "django.db.backends.postgresql_psycopg2"
    database_host = config("DATABASE_HOST", default="localhost")
    database_port = config("DATABASE_PORT", cast=int, default=5432)
    database_name = config("DATABASE_NAME")
    database_password = config("DATABASE_PASSWORD", default="postgres")
    database_user = config("DATABASE_USER", default="postgres")

    # Define databases
    DATABASES = {
        "default": {
            "ENGINE": database_engine,
            "NAME": database_name,
            "USER": database_user,
            "PASSWORD": database_password,
            "HOST": database_host,
            "PORT": database_port,
        }
    }

# Set default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ STATIC AND MEDIA FILES
# └─────────────────────────────────────────────────────────────────────────────────────

# Define static files directories (for collectstatic)
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Determine whether to use local storage
USE_LOCAL_STORAGE = ENVIRONMENT == LOCAL and config(
    "USE_LOCAL_STORAGE", cast=bool, default=True
)

# Check if should use local storage
if USE_LOCAL_STORAGE:

    # Set static URL and static root
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    # Set media URL and media root
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Otherwise handle AWS configuration
else:

    # Retrieve AWS credentials from .env
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")

    # Set AWS static bucket name and domain
    AWS_STATIC_BUCKET_NAME = config("AWS_STATIC_BUCKET_NAME")
    AWS_S3_STATIC_DOMAIN = f"{AWS_STATIC_BUCKET_NAME}.s3.amazonaws.com"

    # Set AWS storage bucket name and domain
    AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_STORAGE_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # Define S3 Object Parameters
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

    # Set static and media file location
    STATICFILES_LOCATION = "static"
    MEDIAFILES_LOCATION = "media"

    # Set static and media file configuration
    STATICFILES_STORAGE = "config.storages.StaticStorage"
    DEFAULT_FILE_STORAGE = "config.storages.MediaStorage"

    # Construct static and media file URLs
    STATIC_URL = f"https://{AWS_S3_STATIC_DOMAIN}/{STATICFILES_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_STORAGE_DOMAIN}/{MEDIAFILES_LOCATION}/"

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK
# └─────────────────────────────────────────────────────────────────────────────────────

# Define Django REST Framework settings
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PARSER_CLASSES": ("rest_framework.parsers.JSONParser",),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}

# Check if browsable API is enabled
if ENABLE_BROWSABLE_API:

    # Restrict renderers to JSON renderer
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"].append(
        "dynamic_rest.renderers.DynamicBrowsableAPIRenderer"
    )

# Define Dynamic REST settings
DYNAMIC_REST = {
    "DEBUG": DEBUG,
    "ENABLE_BROWSABLE_API": ENABLE_BROWSABLE_API,
    "ENABLE_LINKS": True,
    "ENABLE_SERIALIZER_CACHE": True,
    "ENABLE_SERIALIZER_OPTIMIZATIONS": True,
    "DEFER_MANY_RELATIONS": False,
    "MAX_PAGE_SIZE": 100,
    "PAGE_QUERY_PARAM": "page",
    "PAGE_SIZE": 20,
    "PAGE_SIZE_QUERY_PARAM": "page_size",
    "ADDITIONAL_PRIMARY_RESOURCE_PREFIX": "+",
    "ENABLE_HOST_RELATIVE_LINKS": True,
}

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ REDIS
# └─────────────────────────────────────────────────────────────────────────────────────

# Retrieve Redis URL from .env
REDIS_URL = config("REDISTOGO_URL")

# Set Redis broker settings
BROKER_URL = REDIS_URL
BROKER_TRANSPORT_OPTIONS = {"visibility_timeout": 3600}

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ CELERY
# └─────────────────────────────────────────────────────────────────────────────────────

# Define Celery result backend
CELERY_RESULT_BACKEND = REDIS_URL

# Set Celery always eager setting
CELERY_ALWAYS_EAGER = config("CELERY_ALWAYS_EAGER", cast=bool, default=False)

# Define Celery Beat schedule
CELERY_BEAT_SCHEDULE = {
    "fetch-exchange-rates-every-hour": {
        "task": "fetch-exchange-rates",
        "schedule": crontab(minute=0, hour="*/2"),
    },
}

# Define Celery timezone
CELERY_TIMEZONE = "UTC"

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ HEROKU
# └─────────────────────────────────────────────────────────────────────────────────────

# Activate Django-Heroku
django_heroku.settings(locals(), staticfiles=False, databases=False)
