.PHONY: install lint format test clean

# Create a local virtual environment in the project directory
install:
	poetry config virtualenvs.in-project true
	poetry install

lint: install
	poetry run ruff check .
	poetry run ruff format --check .

format: install
	poetry run ruff format .

test: install
	poetry run pytest

clean:
	rm -rf .venv

all: install lint test
