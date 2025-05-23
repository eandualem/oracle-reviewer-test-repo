import pytest

from calculator import add, describe_operation, divide, multiply, power, square, subtract


def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0


def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(5.5, 1.5) == 4.0


def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(-2, -3) == 6
    assert multiply(0, 100) == 0
    assert multiply(1.5, 2) == 3.0


def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-10, 5) == -2
    assert divide(-10, -2) == 5
    assert divide(0, 1) == 0


def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)


def test_describe_operation():
    """Test the describe operation function."""
    assert describe_operation("add", 2, 3, 5) == ("Performed operation 'add' on 2 and 3, the result was 5.")
    # Check the potentially long line output
    desc = describe_operation("multiply", 12345.67, 89101.11, 1100000000)
    assert "Performed operation 'multiply'" in desc  # Basic check
    assert "1100000000" in desc  # Check for the result


def test_power():
    """Test the power function."""
    assert power(2, 3) == 8
    assert power(0, 0) == 1
    assert power(1, 1) == 1
    assert power(2, 0) == 1


def test_square():
    """Test the square function."""
    assert square(2) == 4
    assert square(0) == 0
    assert square(1) == 1
    assert square(-1) == 1
