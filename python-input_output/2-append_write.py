#!/usr/bin/python3
"""This module defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append text to a UTF8 file and return the number of characters added.

    The file is created if it does not exist.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
