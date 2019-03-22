FROM python:3.6-alpine

COPY . /app

RUN pip install -r /app/requirements.txt

CMD ["gunicorn", "-b 0.0.0.0:5000", "-w 4", "certificates:create_app"]
