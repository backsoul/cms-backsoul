FROM python:3.8

ENV PYTHONNUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN python -m pip install -r requirements.txt
COPY . /app/
