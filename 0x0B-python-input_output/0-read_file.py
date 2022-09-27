#!/usr/bin/python3

"""This Module contains 
function that read a text file
and prints it to stdout
"""


def read_file(filename=""):
    """This function read a text file
    and prints it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
