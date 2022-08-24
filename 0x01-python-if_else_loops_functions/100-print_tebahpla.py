#!/usr/bin/python3
for i in reversed(range(97, 123)):
    print("{}".format(chr(i - (32 * (i % 2)))), end="")
