#!/usr/bin/python3
"""Module that multiplies two matrices.

This module defines the function matrix_mul, which returns the product of
two matrices. Both matrices must be non empty rectangular lists of lists of
integers or floats, and the number of columns of the first matrix must be
the number of rows of the second one.
"""


def matrix_mul(m_a, m_b):
    """Multiply the matrix m_a by the matrix m_b and return the result.

    Args:
        m_a (list): the first matrix, a list of lists of numbers.
        m_b (list): the second matrix, a list of lists of numbers.

    Raises:
        TypeError: if a matrix is not a list of lists of numbers or is not
            a rectangle.
        ValueError: if a matrix is empty or if the matrices can't be
            multiplied.
    """
    matrices = (("m_a", m_a), ("m_b", m_b))
    for name, matrix in matrices:
        if not isinstance(matrix, list):
            raise TypeError("{} must be a list".format(name))
    for name, matrix in matrices:
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError("{} must be a list of lists".format(name))
    for name, matrix in matrices:
        if len(matrix) == 0 or all(len(row) == 0 for row in matrix):
            raise ValueError("{} can't be empty".format(name))
    for name, matrix in matrices:
        for row in matrix:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError(
                        "{} should contain only integers or floats".format(
                            name))
    for name, matrix in matrices:
        for row in matrix:
            if len(row) != len(matrix[0]):
                raise TypeError(
                    "each row of {} must be of the same size".format(name))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return [[sum(row[k] * m_b[k][j] for k in range(len(m_b)))
             for j in range(len(m_b[0]))] for row in m_a]
