#!/usr/bin/python3

"""
This module contains function to get an object attributes
and methods
"""


def lookup(obj):
    """
    This function return the list of available
    attributes and methods of obj.
    """
    return dir(obj)
