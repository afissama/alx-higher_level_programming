#!/usr/bin/python3
"""This module contains
    =>append_write
"""


def append_write(filename="", text=""):
    """This function append text to file
    filename
    """
    nb = 0
    with open(filename, 'a', encoding="utf-8") as f:
        nb += f.write(text)
    return nb
