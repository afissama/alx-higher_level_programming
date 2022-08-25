#!/usr/bin/python3
from inspect import getmembers, isfunction
if __name__ == "__main__":
    import hidden_4
    for memb in getmembers(hidden_4, isfunction):
        if not memb[0].startswith("__"):
            print(memb[0])
