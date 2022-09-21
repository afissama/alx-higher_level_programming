#!/usr/bin/python3
"""
This module supplies one function its add two integer example
>>> add_integer(4, 3)
7
"""
def add_integer(a, b=98):
    """ 
    Returns a+b
    """
    a_ = 0
    b_ = 0
    try:
        a_ = int(a)
    except Exception:
        raise TypeError("a must be an integer")
    try:
        b_ = int(b)
    except Exception:
        raise TypeError("b must be an integer")
    
    return (a_ + b_)
