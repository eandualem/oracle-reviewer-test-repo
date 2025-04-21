# Oracle Reviewer Test Repo

This is a simple Python calculator project created specifically for testing the [Oracle PR Reviewer](https://github.com/Rizz-Buzz/Oracle) system (or your equivalent).

It contains:

- Basic calculator functions (`calculator.py`).
- Unit tests using `pytest` (`tests/test_calculator.py`).
- Project configuration using Poetry (`pyproject.toml`).
- Linting and formatting with Ruff.
- Task automation with a Makefile.

## Purpose

The primary goal of this repository is to provide a public, easily accessible codebase to trigger and test the different stages of the Oracle PR Reviewer pipeline, such as:

- Repository cloning and initialization.
- Project analysis.
- Style checking.
- Test execution.
- Context building.
- Review generation and validation.

## Setup

1. Clone the repository (no special authentication needed as it's public).
2. Install Poetry if you don't have it already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
3. Install project dependencies:
   ```bash
   make install
   ```
   Alternatively, you can run:
   ```bash
   poetry install
   ```

## Available Commands

The project uses a Makefile to simplify common tasks:

- `make install`: Install all project dependencies
- `make lint`: Run linting checks on the codebase
- `make format`: Apply automatic formatting to the codebase
- `make test`: Run the test suite
- `make all`: Run install, lint, and test in sequence
