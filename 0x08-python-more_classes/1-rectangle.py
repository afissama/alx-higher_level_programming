#!/usr/bin/python3
"""
A Basic module for rectangle representation.
"""


class Rectangle:
    """ Simple class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.__set_height(height)
        self.__set_width(width)

    def __get_width(self):
        """ Get the width """
        return self.__width

    def __set_width(self, value):
        """ Set the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def __get_height(self):
        """ Get the height """
        return self.__height

    def __set_height(self, value):
        """ Set the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    width = property(__get_width, __set_width)
    height = property(__get_height, __set_height)