#!/usr/bin/python3
"""This module defines a class LockedClass with a locked set of attributes."""


class LockedClass:
    """This class only allows the instance attribute first_name."""
    __slots__ = ["first_name"]
