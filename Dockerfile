FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
RUN pip install poetry
WORKDIR /app
COPY . /app
RUN poetry install
CMD ["python3", "app.py"]