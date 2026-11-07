#!/usr/bin/python3
"""This module defines a class Square that can be printed directly."""


class Square:
    """This class represents a square with a private size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): the size of the new square.
            position (tuple): the offset used when printing the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get or set the position of the square when it is printed."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after validating the value.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        valid = isinstance(value, tuple) and len(value) == 2
        if valid:
            valid = all(isinstance(n, int) and n >= 0 for n in value)
        if not valid:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # at its position."""
        print(str(self))

    def __str__(self):
        """Return the square drawn with # at its position."""
        if self.__size == 0:
            return ""
        lines = ["" for _ in range(self.__position[1])]
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
