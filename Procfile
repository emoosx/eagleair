web: python manage.py bower install
web: python manage.py collectstatic --ignore=.scss
web: gunicorn eagleair.wsgi --log-file -
