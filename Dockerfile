FROM python:3.7-alpine3.10

RUN pip3 install requests

COPY ./src /app

ENTRYPOINT ["python3", "/app/app.py"]
