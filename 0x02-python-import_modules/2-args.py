#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    import sys
    argv = sys.argv
    str_arg = "arguments"
    if len(argv) == 1:
        str_arg = "arguments."
    if len(argv) == 2:
        str_arg = "argument"
    print("{} {}".format(len(argv) - 1, str_arg))
    for i in range(1, len(argv)):
        print("{}: {}".format((i), argv[i]))
