#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [(elm if elm != search else replace) for elm in my_list]
