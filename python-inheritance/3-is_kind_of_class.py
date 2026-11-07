#!/usr/bin/python3
"""This module defines a function that checks the class family of an object."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass of it."""
    return isinstance(obj, a_class)
