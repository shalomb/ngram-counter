FROM debian:buster-slim

LABEL description='Image to run bigram.py'

RUN apt update -y && \
    apt install -y make && \
    mkdir -p /venv/

COPY ./ /venv/

RUN cd /venv/ && \
    make venv

