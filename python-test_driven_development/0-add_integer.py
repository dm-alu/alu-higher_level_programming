#!/usr/bin/python3
"""Module that adds two numbers.

This module defines the function add_integer, which adds two integers.
Floats are accepted too, and they are cast to integers before the addition.
Any other type of argument raises a TypeError.
"""


def add_integer(a, b=98):
    """Add two integers and return the result as an integer.

    Args:
        a (int or float): the first number.
        b (int or float): the second number, 98 by default.

    Raises:
        TypeError: if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
