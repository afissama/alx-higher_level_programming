#!/usr/bin/python3
def magic_string():
    magic_string.count = 1 if not hasattr(magic_string, "count") else magic_string.count + 1
    return ("BestSchool, " * magic_string.count)[:-2]
