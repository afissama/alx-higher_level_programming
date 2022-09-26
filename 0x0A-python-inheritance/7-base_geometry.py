#!/usr/bin/python3
"""
This module is about a Base Geometry class
"""


class BaseGeometry:
    """
    Base geometry class
    """
    def area(self):
        """Raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if not type(value) == int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
