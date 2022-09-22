#!/usr/bin/python3


""" Module to manage square draw
>>> print_square(2)
##
##
"""


def print_square(size):
    """ Print a square of side size
    size must be an integer
    if size is not integer TypeError will be raised
    if size > 0 , valuerror will be raised
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print("\n" . join(["" . join([
                                    ("#" * size)
                                ])] * size))
