#!/usr/bin/python3

"""
This is a simple module which contains one function
print first and last name according to inputs
>>>say_my_name("afis", "Malick")
My name is afis Malick
"""


def say_my_name(first_name, last_name=""):
    """
    print first and last name according to inputs
    >>>say_my_name("afis", "Malick")
    My name is afis Malick
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
