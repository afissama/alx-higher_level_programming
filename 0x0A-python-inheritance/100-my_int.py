#!/usr/bin/python3
"""Module herite from int class"""


class MyInt(int):
    """This class is a subclass of int"""
    def __eq__(self, other):
        """Return != operator value"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return == operator value"""
        return super().__eq__(other)
