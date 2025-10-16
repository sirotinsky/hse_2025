FROM python:3.11
WORKDIR /app
COPY . /app
ENV TZ="Europe/Moscow"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt -y update
RUN apt -y upgrade
RUN apt -y install python3-pip python3-venv python3-dev build-essential libpq-dev libssl-dev libffi-dev python3-setuptools supervisor curl
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir