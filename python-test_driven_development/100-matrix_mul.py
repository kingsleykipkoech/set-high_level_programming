#!/usr/bin/python3
"""Module for matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a: first matrix (list of lists of int/float)
        m_b: second matrix (list of lists of int/float)

    Returns:
        new matrix result of m_a * m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(r, list) for r in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(r, list) for r in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(
                    "m_a should contain only integers or floats"
                )
    for row in m_b:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(
                    "m_b should contain only integers or floats"
                )
    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")
    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            total = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(total)
        result.append(row)
    return result
