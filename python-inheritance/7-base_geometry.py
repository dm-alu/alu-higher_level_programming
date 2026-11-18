#!/usr/bin/python3
"""Module that defines the BaseGeometry class with an integer validator."""


class BaseGeometry:
    """BaseGeometry class that validates the values of geometry classes."""

    def area(self):
        """Raise an exception because the area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
