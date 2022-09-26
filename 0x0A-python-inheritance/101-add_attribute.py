#!/usr/bin/python3
"""This module contains this fucntions:
    =>add_attribute
"""


def add_attribute(obj, name, value):
    """Add attribute to object
    or raise exception
    """
    if not hasattr(obj, name):
        if not hasattr(obj, '__dict__'):
            raise TypeError("can't add new attribute")
        else:
            setattr(obj, name, value)
