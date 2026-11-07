#!/usr/bin/python3
"""This module defines a class Square that can be compared by area."""


class Square:
    """This class represents a square that compares to others by area."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int or float): the size of the new square.
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
            TypeError: if value is not a number (int or float).
            ValueError: if value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if both squares have the same area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if the squares have different areas."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this square has a smaller area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square has a smaller or equal area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this square has a bigger area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square has a bigger or equal area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()
