#!/usr/bin/python3
"""This module contains a function
"""


def append_after(filename="", search_string="", new_string=""):
    """Replace in file after occurence"""
    str_ = ""
    with open(filename, 'r') as f:
        for line in f:
            str_ += line
            if search_string in line:
                str_ += new_string
    with open(filename, 'w') as f:
        f.write(str_)
