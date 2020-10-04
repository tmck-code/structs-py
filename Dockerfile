FROM python:3.8-slim

WORKDIR /home/python

ADD requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

ADD . .
