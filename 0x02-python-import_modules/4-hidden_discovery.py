#!/usr/bin/python3
from inspect import getmembers, isfunction
if __name__ == "__main__":
    import hidden_4
    for memb in dir(hidden_4):
        if not memb.startswith("__"):
            print(memb)
