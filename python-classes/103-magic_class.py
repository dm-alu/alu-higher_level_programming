#!/usr/bin/python3
"""This module defines the class MagicClass, a circle of a given radius."""
import math


class MagicClass:
    """This class represents a circle with a private radius."""

    def __init__(self, radius=0):
        """Initialize a new circle.

        Args:
            radius (int or float): the radius of the circle.

        Raises:
            TypeError: if radius is not an integer or a float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
