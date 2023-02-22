#!/usr/bin/env bash

./pom-54-team-12/docker/scripts/wait-for-it.sh postgres:5432 -s -t 30-
python pom-54-team-12/library/manage.py migrate
python pom-54-team-12/library/manage.py runserver 0.0.0.0:8000 || { echo 'runserver failed' ; exit 1; }
