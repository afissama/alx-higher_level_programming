#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    return [(my_list[i] if i != idx else element) for i in range(len(my_list))]
