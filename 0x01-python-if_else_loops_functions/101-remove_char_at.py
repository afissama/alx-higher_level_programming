#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        _str = str
    else:
        _str = str[:n] + str[n+1:]
    return _str
