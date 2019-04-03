# /bin/sh
python3 manage.py init
gunicorn -b 0.0.0.0:5000 -w 4 'certificates:create_app()'