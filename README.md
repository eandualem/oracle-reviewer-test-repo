# Oracle Reviewer Test Repo

This is a simple Python calculator project created specifically for testing the [Oracle PR Reviewer](https://github.com/Rizz-Buzz/Oracle) system (or your equivalent).

It contains:

- Basic calculator functions (`calculator.py`).
- Unit tests using `pytest` (`tests/test_calculator.py`).
- Minimal configuration files.

## Purpose

The primary goal of this repository is to provide a public, easily accessible codebase to trigger and test the different stages of the Oracle PR Reviewer pipeline, such as:

- Repository cloning and initialization.
- Project analysis.
- Style checking.
- Test execution.
- Context building.
- Review generation and validation.

## Setup

1.  Clone the repository (no special authentication needed as it's public).
2.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

To run the unit tests, execute the following command from the root directory:

```bash
pytest
```
