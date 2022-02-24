from .base import *
import django_heroku

ALLOWED_HOSTS += ["*"]

INSTALLED_APPS += [
    # Internal Apps

    # External Apps
    
]

MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        "rest_framework.renderers.JSONRenderer",
    )
}

TEMPLATES += []

DATABASES = {}

AUTH_PASSWORD_VALIDATORS += []

django_heroku.settings(locals())
