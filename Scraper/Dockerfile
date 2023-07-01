FROM python:3.9.6

WORKDIR /app

COPY . .

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "nano"]
RUN pip install  -r requirements.txt


CMD scrapy crawl gallito