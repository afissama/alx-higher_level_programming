#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0] if len(my_list) > 0 else None
    for i in range(len(my_list)):
        if (max < my_list[i]):
            max = my_list[i]
    return (max)
