#!/usr/bin/python3
def roman_to_int(roman_string):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sub = {'I': "VX", 'X': "LC", 'C': "DM"}
    value = 0
    i = 0
    str_ = roman_string
    while (i < len(str_)):
        if (str_[i] in sub.keys()):
            nxt = i + 1
            if ((nxt < len(str_)) and (str_[nxt] in sub[str_[i]])):
                value = value + (symbols[str_[nxt]] - symbols[str_[i]])
                i = nxt + 1
                continue
        value = value + symbols[str_[i]]
        i = i + 1
    return (value)
