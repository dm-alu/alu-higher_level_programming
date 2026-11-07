#!/usr/bin/python3
"""This module defines a list class that can print itself sorted."""


class MyList(list):
    """This class is a list with a method that prints it sorted."""

    def print_sorted(self):
        """Print the list in ascending order without changing the list."""
        print(sorted(self))
