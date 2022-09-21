#!/usr/bin/python3


class Rectangle:
    """ Simple class Rectangle"""
    
    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.height = height
        self.width = width

    def width(self):
        """ Get the width """
        return self.__width
    
    def width(self, value):
        """ Set the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value
    
    def height(self):
        """ Get the height """
        return self.__height

    def height(self, value):
        """ Set the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value
    width = property(width, width)
    height = property(height, height)