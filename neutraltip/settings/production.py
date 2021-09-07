from .base import *

import os
import environ
import django_heroku

env = environ.Env(
    DEBUG=(bool, False),
)

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

DATABASES['default']['CONN_MAX_AGE'] = 60

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Whitenoise gzip compression
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Activate Django-Heroku.
django_heroku.settings(locals())
