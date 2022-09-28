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
        tmp = {}
        for x in sorted(vars(self).keys()):
            tmp[x] = vars(self)[x]
        return tmp

    def to_json(self, attrs=None):
        """Return dict representation of the class
        based on attrs.
        """
        is_list_of_str = 0
        if isinstance(attrs, list) and len(attrs) > 1:
            for i in attrs:
                if not isinstance(i, str):
                    break
            is_list_of_str = 1

        if is_list_of_str == 0:
            tmp = {}
            for x in sorted(vars(self).keys()):
                tmp[x] = vars(self)[x]
            return tmp
        else:
            tmp = {}
            for x in sorted(attrs):
                if x in vars(self).keys():
                    tmp[x] = vars(self)[x]
            return tmp
