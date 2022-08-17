FROM python:3.9.13-buster

WORKDIR /playwright_test

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN playwright install chromium

COPY . .

RUN useradd -m myuser
USER myuser

         
CMD python3 playwright_test/pw_codegen.py