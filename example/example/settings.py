# vim: ts=4 sw=4 et:
# Django settings for example project.
from os.path import dirname

from example.util import (
    parse_url,
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

OAUTH2_PROVIDERS = { 
    "google": { 
        "client_id": "421833888173.apps.googleusercontent.com",
        "client_secret": "VueqKFZyz-aoL4rQFleEIT1j",
        "auth_endpoint": "https://accounts.google.com/o/oauth2/auth",
        "token_endpoint": "https://accounts.google.com/o/oauth2/token",
        "resource_endpoint": "https://www.googleapis.com/oauth2/v1",
        "scope": ("email", "https://www.googleapis.com/auth/userinfo.profile",)
    },
    "facebook": {
        "client_id": "152107704926343",
        "client_secret": "80c81e4d7d5bc68ecc8cf1da0213382e",
        "auth_endpoint": "https://www.facebook.com/dialog/oauth",
        "token_endpoint": "https://graph.facebook.com/oauth/access_token",
        "resource_endpoint": "https://graph.facebook.com",
        "scope": ("email",),
        "parser": parse_url
    },
    "github": {
        "client_id": "12837d83a5d8b94f605b",
        "client_secret": "2261a9513a65007c16be0a8978b600db1f64dd14",
        "auth_endpoint": "https://github.com/login/oauth/authorize",
        "token_endpoint": "https://github.com/login/oauth/access_token",
        "resource_endpoint": "https://api.github.com",
        "parser": parse_url
    },
    "stackexchange": {
        "client_id": "543",
        "client_secret": "pbLJjRO3bk)*J12OKfDbMw((",
        "auth_endpoint": "https://stackexchange.com/oauth",
        "token_endpoint": "https://stackexchange.com/oauth/access_token",
        "resource_endpoint": "https://api.stackexchange.com/2.0",
        "parser": parse_url
    },
    }

OAUTH2_EXCEPTION_URL = "/o/error"
OAUTH2_AUTH_FN = "example.auth.authenticate"

AUTHENTICATION_BACKENDS = (
    "django_sanction.backends.AuthenticationBackend",
    "django.contrib.auth.backends.ModelBackend",
)


ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sql.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8bh_109l=0$w(32c+j-o!+rxl$6snhm$!^874ku8h*p_2&amp;((ll'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_sanction.middleware.ResourceMiddleware",
)

ROOT_URLCONF = 'example.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'example.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	"%s/templates" % dirname(__file__),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    "reversetag",
    "django_sanction",
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

