#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    _a = tuple_a + (0, 0)
    _b = tuple_b + (0, 0)
    return ((_a[0] + _b[0], _a[1] + _b[1]))
