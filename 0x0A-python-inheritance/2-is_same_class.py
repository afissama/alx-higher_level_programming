#!/usr/bin/python3
"""
This module contains this functions:
=> is_same_class
"""


def is_same_class(obj, a_class):
    """
    Return True if the object argument
    is exactly an instance of the classinfo argument
    """
    return type(obj) == a_class
