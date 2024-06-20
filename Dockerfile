FROM python:3.12

RUN apt-get update && apt install -y tzdata && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml ./
RUN pip install poetry
#RUN poetry config virtualenvs.create false
#RUN poetry config virtualenvs.in-project false
RUN poetry update
#RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
#RUN pip install -r requirements.txt

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

COPY app ./
COPY database ./
COPY manage.py ./
