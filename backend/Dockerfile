FROM python:3.10.10

WORKDIR /usr/src/app/simpt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/app/simpt
RUN pip install -r requirements.txt

COPY simpt /usr/src/app/simpt

EXPOSE 8000
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && gunicorn simpt.wsgi -b 0.0.0.0:8000"]
