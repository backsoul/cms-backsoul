FROM python:3.8

ENV PYTHONNUNBUFFERED 1
RUN mkdir /cms-backsoul
WORKDIR /cms-backsoul
COPY requirements.txt /cms-backsoul/
RUN python -m pip install -r requirements.txt
COPY . /cms-backsoul/
