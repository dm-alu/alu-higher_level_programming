#!/usr/bin/python3
"""This module defines a function that adds an attribute to an object."""


def add_attribute(obj, name, value):
    """Add the attribute name with the given value to obj if it is allowed.

    Raises:
        TypeError: if the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
