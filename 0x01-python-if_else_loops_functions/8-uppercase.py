#!/usr/bin/python3
def uppercase(str):
    _str = ""
    for i in range(len(str)):
        c = str[i]
        if ord(str[i]) >= 97 and ord(str[i]) <= 123:
            c = chr(ord(str[i]) - 32)
        _str += c
    print("{}".format(_str))
