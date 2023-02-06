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
        """Validates Integer values and raises
        exception if necessary
        """
        if not isinstance(value, int):
            raise TypeError(str(name) + " must be an integer")
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")
