#!/usr/bin/python3


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

    def area(self):
        """ Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """ Compute perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.height + self.width)

    def __str__(self):
        """String representation
        Rectange
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n" . join(["" . join([("#" * self.width)])] * self.height)

    def __repr__(self):
        """String representation
        Rectange
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    width = property(__get_width, __set_width)
    height = property(__get_height, __set_height)
