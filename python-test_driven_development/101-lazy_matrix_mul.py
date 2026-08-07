#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using numpy.

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        numpy matrix result of m_a * m_b
    """
    return np.matmul(m_a, m_b)
