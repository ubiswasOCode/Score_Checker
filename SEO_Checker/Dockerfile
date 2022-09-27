FROM python:3.8.12
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update
RUN apt-get install tesseract-ocr -y
RUN apt-get install libtesseract-dev -y
RUN pip3 install -r requirements.txt
COPY . /code/
