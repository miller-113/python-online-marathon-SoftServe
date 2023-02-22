FROM python:3.10-slim

COPY . /app
# запускается когда строим образ
WORKDIR /app/library
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

#EXPOSE 8010

# запускается при запуске контейнера
#CMD ["python", "manage.py", "runserver", "--noreload"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]