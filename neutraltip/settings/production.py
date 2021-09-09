from .base import *

import os
import environ
import django_heroku

env = environ.Env(
    DEBUG=(bool, False),
)

SECRET_KEY = 'django-insecure-+-sxd16*k5i=8na*#72q3g_(mls-u2mbiecq8)4m($dt_gfx1b'

DEBUG = False

ALLOWED_HOSTS = ['*']

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

DATABASES['default']['CONN_MAX_AGE'] = 60

# Whitenoise compression

# Activate Django-Heroku.
django_heroku.settings(locals(), staticfiles=False)