FROM python:3.6

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install -r requirements.txt --default-timeout=1000 --no-cache-dir
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]