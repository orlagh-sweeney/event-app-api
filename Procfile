release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf_event_api.wsgi