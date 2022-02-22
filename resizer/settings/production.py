from .base import *

ALLOWED_HOSTS += []

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