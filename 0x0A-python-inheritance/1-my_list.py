#!/usr/bin/python3
"""
This module contains a class that herit list
"""


class MyList(list):
    """
    This class inherits from list
    and add a new method to it
    """

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
