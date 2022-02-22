import os
from decouple import config
from django.core.wsgi import get_wsgi_application

PRODUCTION = config("PRODUCTION", cast = bool)

if PRODUCTION:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resizer.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resizer.settings.development')

application = get_wsgi_application()
