python manage.py collectstatic --noinput
python3 manage.py migrate
uwsgi --strict --ini uwsgi.ini