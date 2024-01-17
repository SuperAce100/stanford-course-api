FROM python:3.9

RUN pip install flask requests xmltodict gunicorn

COPY src/ /app
WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app
