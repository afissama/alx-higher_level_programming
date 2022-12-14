#!/usr/bin/python3
"""
This module is about a square Geometry class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size):
        """Call while instantiate the class"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
