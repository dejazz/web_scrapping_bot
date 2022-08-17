FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3.9
RUN apt install -y python3-pip

COPY app/ /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN playwright install --with-deps chromium

CMD ....