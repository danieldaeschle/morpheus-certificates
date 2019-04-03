FROM python:3.6-alpine

COPY . /app

WORKDIR /app

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "init", "&&", "gunicorn", "-b 0.0.0.0:5000", "-w 4", "certificates:create_app()"]
