FROM python:3.10

WORKDIR /opt/converter

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'config.settings'
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240

COPY requirements.txt requirements.txt
COPY ./uwsgi/uwsgi.ini uwsgi.ini

RUN  mkdir -p /var/www/static/ \
     && mkdir -p /var/www/media/ \
     && mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/movies/static/ \
     && mkdir -p /opt/app/media/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["bash", "entrypoint.sh"]