#!/usr/bin/python3
"""Module for matrix division function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix: list of lists of integers or floats
        div: number to divide by

    Returns:
        new matrix with all elements divided by div, rounded to 2 decimals
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    row_len = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(msg)
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) for el in row] for row in matrix]
