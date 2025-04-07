# calculator.py

"""A simple calculator module."""


def add(x: float, y: float) -> float:
    """Adds two numbers."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Subtracts the second number from the first."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Multiplies two numbers."""
    # Intentionally inconsistent spacing below for style check testing
    result = x * y
    return result


def divide(x: float, y: float) -> float:
    """
    Divides the first number by the second.
    Raises ValueError if the divisor is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    # Potential minor issue: Integer division if only integers were intended?
    # Or maybe just check for non-numeric types? Let's keep it simple for now.
    return x / y


# Example of a slightly too long line for linters
def describe_operation(op_name: str, num1: float, num2: float, result: float) -> str:
    """Provides a string description of the operation performed, potentially exceeding line limits."""
    return f"Performed operation '{op_name}' on {num1} and {num2}, the result was {result}."
