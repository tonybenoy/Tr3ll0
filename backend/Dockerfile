FROM python:latest
RUN apt update -y
RUN apt upgrade -y

ADD ./backend/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./backend/tr3ll0 /app