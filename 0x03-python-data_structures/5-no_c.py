#!/usr/bin/env python3
def no_c(my_string):
    str = ""
    for i in range(len(my_string)):
        if not ord(my_string[i]) in [67, 99]:
            str += my_string[i]
    return (str)
