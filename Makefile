.PHONY: setup dev test lint format

setup:
	poetry install

dev:
	poetry install --with dev
	poetry run pre-commit install

test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run black .
