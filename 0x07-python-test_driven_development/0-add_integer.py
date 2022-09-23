#!/usr/bin/python3
"""
This module supplies one function its add two integer example
>>> add_integer(4, 3)
7
"""


def add_integer(a, b=98):
    """
    Returns a+b
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
