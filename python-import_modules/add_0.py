#!/usr/bin/python3

def add(a: int, b: int) -> int:
    """Adds two integers.

    Args:
        a (int): The first integer to be added.
        b (int): The second integer to be added.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If either a or b is not an integer.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return a + b

