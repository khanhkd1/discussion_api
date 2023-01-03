FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY api/ .
COPY config/ .
COPY manage.py .
# COPY . .