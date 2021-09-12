from .base import *

import os
import environ
import django_heroku

env = environ.Env(
    DEBUG=(bool, False),
)

SECRET_KEY = 'django-insecure-+-sxd16*k5i=8na*#72q3g_(mls-u2mbiecq8)4m($dt_gfx1b'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'cloudinary_storage',
    'cloudinary',
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'vaibhavkacloud',
    'API_KEY': '592713423378895',
    'API_SECRET': 'vK5NsPMIo95510tnaf-kA_Vz_Ds'
}

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

DATABASES['default']['CONN_MAX_AGE'] = 60

# Whitenoise compression
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Media settings
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.RawMediaCloudinaryStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Activate Django-Heroku.
django_heroku.settings(locals(), staticfiles=False)