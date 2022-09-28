#!/usr/bin/python3

"""
This module return list of list of pascal triangle
"""


def pascal_triangle(n):
    """Print pascal triangle for n"""
    if n <= 0:
        return []

    my_list = [[1]]
    for i in range(1, n):
        my_list.append([1])
        for j in range(1, i + 1):
            x_ = 0 if len(my_list[i-1]) - 1 < j else my_list[i-1][j]
            y_ = 0 if len(my_list[i-1]) - 1 < j - 1 else my_list[i - 1][j - 1]
            my_list[i].append(x_ + y_)

    return my_list
