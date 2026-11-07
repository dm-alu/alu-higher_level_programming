#!/usr/bin/python3
"""This module defines a class Square with a private size attribute."""


class Square:
    """This class represents a square defined by its private size."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size: the size of the new square, with no type or value check.
        """
        self.__size = size
