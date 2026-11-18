#!/usr/bin/python3
"""Module that divides the elements of a matrix.

This module defines the function matrix_divided, which divides every element
of a matrix by a number and returns a new matrix. The results are rounded
to two decimal places and the original matrix is left unchanged.
"""


def matrix_divided(matrix, div):
    """Divide all the elements of a matrix by div and return a new matrix.

    Args:
        matrix (list): a list of lists of integers or floats, with rows of
            the same size.
        div (int or float): the number that divides every element.

    Raises:
        TypeError: if matrix is not a list of lists of numbers, if the rows
            have different sizes, or if div is not a number.
        ZeroDivisionError: if div is equal to 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
