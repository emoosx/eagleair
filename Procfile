web: python manage.py bower install
web: python manage.py collectstatic
web: gunicorn eagleair.wsgi --log-file -
