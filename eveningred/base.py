from pathlib import Path
import os
import json
# import logging
from django.contrib.messages import constants as messages

# Application paths
# =====================================================================
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# https://docs.djangoproject.com/en/3.2/howto/static-files/
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATIC_URL = '/assets/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')


# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-MEDIA_URL
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Security settings
# =====================================================================
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
with open(BASE_DIR / 'eveningred/secrets_development.json') as secrets:
    secrets = json.load(secrets)

SECRET_KEY = secrets['SECRET_KEY']
KEY_POSTCODENL = 'bnEyM3ZIUGFld3JzMktHenM5VGlCMko0ZnZTdG1xdElEU0c4OGlpc0JWNzp5MkkwOHBBcEpXb0cxMUhjcDJuVzFGVEhtazZ5WnVEQUlCdHpybVNiT1RlckdSdlozWQ=='
ALLOWED_HOSTS = ['*']
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SESSION_COOKIE_DOMAIN = None  # NEW RULE 01-05-2021
SESSION_COOKIE_AGE = 36000  # on hour in seconds 900 = 15 min 3600 = 1 uur
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CSRF_TRUSTED_ORIGINS = ['https://*.eveningred.nl', 'https://klant1.eveningred.nl']

# App  definition
# =====================================================================
SHARED_APPS = [
    'django_tenants',  # mandatory, should always be before any django app
    'tenants',  # you must list the app where your tenant model resides in
    'django.contrib.contenttypes',  # this one always here
]

TENANT_APPS = [
    'django.contrib.contenttypes',
    # your tenant-specific apps
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'prettyjson',
    'localflavor',
    'debug_toolbar',
    'import_export',
    'crispy_forms',
    'crispy_bootstrap5',
    'qr_code',
    'tinymce',
    'core',
    'applog',
    'articles',
    'configuration',
    'dashboard',
    'emails',
    'hours',
    'master',
    'materials',
    'overviews',
    'projects',
    'public',
    'relations',
    'shared',
    'users',
]

INSTALLED_APPS = [
    'django_tenants',  # mandatory, should always be before any django app
    'tenants',  # you must list the app where your tenant model resides in
    'django.contrib.contenttypes',  # this one always here
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'prettyjson',
    'localflavor',
    'debug_toolbar',
    'import_export',
    'crispy_forms',
    'crispy_bootstrap5',
    'qr_code',
    'tinymce',
    'core',
    'applog',
    'articles',
    'configuration',
    'dashboard',
    'emails',
    'hours',
    'master',
    'materials',
    'overviews',
    'projects',
    'public',
    'relations',
    'shared',
    'users',
]

# Cripsy forms
# =====================================================================
CRISPY_ALLOWED_TEMPLATE_PACKS = "mdbootstrap"
CRISPY_TEMPLATE_PACK = 'mdbootstrap'


# Tiny MCE
# =====================================================================
TINYMCE_JS_URL = os.path.join(STATIC_URL, "js/tinymce/tinymce.min.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "js/tinymce/tinymce.min.js")


# Jsignature settings
# =====================================================================
# JSIGNATURE_WIDTH = 500
# JSIGNATURE_HEIGHT = 200
JSIGNATURE_COLOR = "#000"
JSIGNATURE_BACKGROUND_COLOR = "#fff"
JSIGNATURE_DECOR_COLOR = "#fff"
JSIGNATURE_LINE_WIDTH = 1
JSIGNATURE_UNDO_BUTTON = True
JSIGNATURE_RESET_BUTTON = True

# Debug_toolbar
# =====================================================================
INTERNAL_IPS = ['127.0.0.1']

DISABLE_DARK_MODE = True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_COLLAPSED': True,
    'DISABLE_PANELS': {
        'debug_toolbar.panels.history.HistoryPanel',
        'ddt_request_history.panels.request_history.RequestHistoryPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
        'debug_toolbar.panels.versions.VersionsPanel',
    },
}

# Middleware
# =====================================================================
MIDDLEWARE = [
    'django_tenants.middleware.TenantMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'request_logging.middleware.LoggingMiddleware',

    'core.middleware.BaseMiddleware',
]

TENANT_MODEL = "tenants.Tenant"  # app.Model
TENANT_DOMAIN_MODEL = "tenants.Domain"  # app.Model
DEFAULT_FILE_STORAGE = "django_tenants.storage.TenantFileSystemStorage"
PUBLIC_SCHEMA_NAME = 'public'
ROOT_URLCONF = 'eveningred.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',  # if one wants to use {{ MEDIA_URL }} in the templates
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shared.variables.template_variables.add_variables',
            ],
            'builtins': [
                'shared.variables.template_tags',
            ],
        },
    },
]

WSGI_APPLICATION = 'eveningred.wsgi.application'

# Database settings
# =====================================================================
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': secrets['DB_NAME'],
        'USER': secrets['DB_USER'],
        'PASSWORD': secrets['DB_PASSWORD'],
        'HOST': secrets['DB_HOST'],
        'PORT': secrets['DB_PORT'],
    }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

# Email settings
# =====================================================================
EMAIL_HOST = secrets['EMAIL_HOST']
EMAIL_PORT = secrets['EMAIL_PORT']
EMAIL_HOST_USER = secrets['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = secrets['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Eveningred <noreply@eveningred.nl>'

# Password validation and user stuff
# =====================================================================
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
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

AUTH_USER_MODEL = 'users.User'

# Internationalization
# =====================================================================
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'nl-nl'
USE_I18N = True
USE_L10N = True
TIME_ZONE = 'Europe/Amsterdam'
DECIMAL_SEPARATOR = ','

# Default primary key field type
# =====================================================================
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login
# =====================================================================
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = ''
LOGOUT_REDIRECT_URL = '/'
PASSWORD_RESET_TIMEOUT = 172800  # New in 3.1 In seconds this is 2 days
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# reCaptcha v2
# =====================================================================
RECAPTCHA_PUBLIC_KEY = secrets['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = secrets['RECAPTCHA_PRIVATE_KEY']
