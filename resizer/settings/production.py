from .base import *
import django_heroku

ALLOWED_HOSTS += ["*"]

INSTALLED_APPS += [
    # Internal Apps

    # External Apps
    
]

MIDDLEWARE += []

TEMPLATES += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS += []
django_heroku.settings(locals())