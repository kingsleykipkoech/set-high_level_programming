#!/usr/bin/python3
"""Module for integer addition function."""


def add_integer(a, b=98):
    """Adds two integers or floats (cast to int).

    Args:
        a: first number (int or float)
        b: second number (int or float), default 98

    Returns:
        int: the sum of a and b as integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
