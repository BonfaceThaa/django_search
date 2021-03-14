# pull official base image
FROM python:3.8.3-alpine

# create
# set work directory
WORKDIR /django_search

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install pre-requisites
RUN apk add postgresql-dev zlib-dev python3-dev gcc musl-dev build-base linux-headers pcre-dev
# install dependencies
RUN pip install --upgrade pip
COPY django_search/requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .