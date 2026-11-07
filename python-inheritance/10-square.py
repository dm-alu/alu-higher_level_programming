#!/usr/bin/python3
"""This module defines a class Square that is a kind of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents a square, a subclass of Rectangle."""

    def __init__(self, size):
        """Initialize a square after validating its size.

        Args:
            size (int): the size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
