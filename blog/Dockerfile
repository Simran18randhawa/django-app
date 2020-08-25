FROM python: 3.8-alpine

MAINTAINER Simran

COPY requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /code
COPY . /code/
WORKDIR 
