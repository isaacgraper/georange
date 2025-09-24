.PHONY: setup dev test lint format

setup:
	@if ! command -v poetry >/dev/null 2>&1; then \
		@echo "Poetry not found. Installing..."; \
		curl -sSL https://install.python-poetry.org | python3 -; \
		export PATH="$$HOME/.local/bin:$$PATH"; \
	fi
	@echo "Installing project dependencies..."
	@echo "Must have python^3.12"
	poetry install

dev:
	poetry lock
	poetry install --with dev
	poetry run pre-commit install

check:
	poetry run pytest || exit 1
	poetry run ruff check . || exit 1
	poetry run black . || exit 1
	poetry run isort . || exit 1
