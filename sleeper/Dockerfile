FROM python:3.7-slim
RUN apt update && apt install -y \
    python3-dev \
    python3-pip \
    curl
COPY ./requirements.txt /usr/local/src/sleeper
RUN pip3 install -r /usr/local/src/sleeper/requirements.txt
COPY . /usr/local/src/sleeper/
WORKDIR /usr/local/src/sleeper/
