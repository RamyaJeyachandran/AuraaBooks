from .base import *

DEBUG = True

# Add dev only apps
INSTALLED_APPS += []

# Use console backend for email in dev
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': env('REDIS_URL', default='redis://redis:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
