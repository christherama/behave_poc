FROM python:2-jessie
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
