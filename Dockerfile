FROM python:3.11
ENV PYTHONUNBUFFERED 1
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
WORKDIR /placesremember/
RUN python manage.py makemigrations
RUN python manage.py migrate
