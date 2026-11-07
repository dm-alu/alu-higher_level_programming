#!/usr/bin/python3
"""This module defines a function that inserts text after matching lines."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line of a file containing search_string.

    Args:
        filename (str): the path of the UTF8 text file to update.
        search_string (str): the text that selects the lines.
        new_string (str): the text inserted after each selected line.
    """
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
