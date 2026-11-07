#!/usr/bin/python3
"""This module defines a class BaseGeometry with an unimplemented area."""


class BaseGeometry:
    """This class is a base for geometry classes."""

    def area(self):
        """Raise an Exception because area is not implemented here."""
        raise Exception("area() is not implemented")
