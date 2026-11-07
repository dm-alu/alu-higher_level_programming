#!/usr/bin/python3
"""This module defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a UTF8 file and return the number of characters written.

    The file is created if it does not exist and overwritten otherwise.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
