#!/usr/bin/python3
"""This module defines a function that describes an object as a dictionary."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON use."""
    return obj.__dict__.copy()
