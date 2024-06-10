# FastAPI Template for Rocket

## Setup for trial

- use Python 3.12 or later
- install poetry by running `pip install poetry`
- clone this repository
- run `poetry install`
- create postgresql database named 'fastapi_template': `createdb fastapi_template`
- run `poetry run python manage.py db migrate`
- run `poetry run python manage.py db seed`
- run `poetry run python manage.py serve` to start the server

