#!/usr/bin/python3
"""Module that multiplies two matrices with NumPy.

This module defines the function lazy_matrix_mul, which returns the product
of two matrices. The work is done by the matmul function of the NumPy
module, so the errors are the ones raised by NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply the matrix m_a by the matrix m_b using NumPy.

    Args:
        m_a (list): the first matrix, a list of lists of numbers.
        m_b (list): the second matrix, a list of lists of numbers.

    Returns:
        numpy.ndarray: the product of the two matrices.
    """
    return numpy.matmul(m_a, m_b)
