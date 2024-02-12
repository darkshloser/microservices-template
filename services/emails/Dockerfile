FROM python:3.10.6-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN apt update

RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config

RUN pip install -r requirements.txt