#!/usr/bin/python3
"""This module defines a simple class student
"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """Call when class is instantiated"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dict representation of the class"""
        return vars(self)
