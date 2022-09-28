#!/usr/bin/python3
"""This module contains
    =>write_file
"""


def write_file(filename="", text=""):
    """This function writes a string into txt file
    """
    nb = 0
    with open(filename, 'w', encoding="utf-8") as f:
        nb = f.write(text)
    return nb
