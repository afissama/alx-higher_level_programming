#!/usr/bin/python3
"""
This module contain class Base that will be used for all
Class in this project.
"""


class Base:
    """
    Base that will be used for all
    Class in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
