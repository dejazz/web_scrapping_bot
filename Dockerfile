FROM ubuntu:focal

RUN apt update

RUN apt install -y python3.9

RUN apt install -y python3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt 

RUN playwright install --with-deps

COPY . /app

EXPOSE 8000



