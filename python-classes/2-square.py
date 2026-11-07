#!/usr/bin/python3
"""This module defines a class Square that validates its size."""


class Square:
    """This class represents a square defined by its private size."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): the size of the new square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
