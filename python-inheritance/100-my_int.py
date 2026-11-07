#!/usr/bin/python3
"""This module defines a rebel integer class with inverted comparisons."""


class MyInt(int):
    """This class is an int subclass whose == and != are inverted."""

    def __eq__(self, other):
        """Return True when the values differ, as the inverse of =="""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return True when the values are equal, as the inverse of !="""
        return int.__eq__(self, other)

    __hash__ = int.__hash__
