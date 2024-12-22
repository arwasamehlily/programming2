# Oneliner Docstring

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def double(number):
    """Return double the input number."""
    return number * 2

# Multiline Docstring


def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

# Annotations

def divide_numbers(a: float, b: float) -> float:
    """
    Divide one number by another.

    Args:
        a (float): The numerator.
        b (float): The denominator. Must not be zero.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If the denominator is zero.

    Example:
        >>> divide_numbers(10.0, 2.0)
        5.0
    """
    if b == 0:
        raise ValueError("Denominator must not be zero.")
    return a / b
