#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using NumPy."""
    return np.matmul(m_a, m_b)
