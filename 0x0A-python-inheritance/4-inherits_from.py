#!/usr/bin/python3
"""This module is about class type in python
    it contains these functions:
    => inherits_from(obj, a_class):
"""


def inherits_from(obj, a_class):
    """
    Check if obj inherit from a_class
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
