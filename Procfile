release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf__event_api.wsgi