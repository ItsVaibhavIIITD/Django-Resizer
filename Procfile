web: gunicorn resizer.wsgi
release: python manage.py makemigrations core
release: python manage.py collectstatic
release: python manage.py migrate
