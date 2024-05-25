FROM python:3.11

ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-dev libpq-dev build-essential -y
RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev

COPY . /app