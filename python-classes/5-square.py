#!/usr/bin/python3
"""This module defines a class Square that can print itself with #."""


class Square:
    """This class represents a square defined by its private size."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating the value.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #, or an empty line if empty."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
