FROM python:3.12

RUN apt-get update && apt install -y tzdata && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.8.3 \
    POETRY_NO_INTERACTION=1

WORKDIR /app

COPY pyproject.toml ./

RUN pip install poetry==$POETRY_VERSION
RUN poetry config virtualenvs.create true
RUN poetry config virtualenvs.in-project true
RUN poetry update
#RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
#RUN pip install -r requirements.txt

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

COPY . .
