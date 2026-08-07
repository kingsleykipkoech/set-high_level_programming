#!/usr/bin/python3
"""Module for print_square function."""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): the size length of the square
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
