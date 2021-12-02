# syntax=docker/dockerfile:1.3
FROM python:3.10-alpine

RUN --mount=type=cache,mode=0755,target=/var/cache/apk \
    apk update && apk add build-base cmake libffi-dev libffi \
    && mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONPATH=/usr/src/app/

ARG requirement_file="testing.txt"
COPY requirements/. /usr/src/app/requirements
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip \
    pip install -r requirements/$requirement_file

COPY . /usr/src/app

CMD [ "pytest" ]
