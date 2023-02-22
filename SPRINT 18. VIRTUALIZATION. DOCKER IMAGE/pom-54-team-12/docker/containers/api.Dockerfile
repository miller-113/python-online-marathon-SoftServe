FROM python:3.10-slim

RUN apt-get update && apt-get install -y gettext

ADD . /pom-54-team-12

ENV PYTHONPATH ''${PYTHONPATH}/pom-54-team-12''
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN chmod +x /pom-54-team-12/docker/scripts/api.entrypoint.dev.sh && \
    chmod +x /pom-54-team-12/docker/scripts/wait-for-it.sh

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /pom-54-team-12/requirements.txt
