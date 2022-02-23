from .base import *
import django_heroku

ALLOWED_HOSTS += ["*"]

INSTALLED_APPS += [
    # Internal Apps

    # External Apps
    
]

MIDDLEWARE += []

TEMPLATES += []

DATABASES = {}

AUTH_PASSWORD_VALIDATORS += []

django_heroku.settings(locals())