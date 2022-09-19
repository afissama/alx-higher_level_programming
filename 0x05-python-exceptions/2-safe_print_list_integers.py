#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pos = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            pos = pos + 1
        except ValueError:
            continue
        except TypeError:
            continue
    print("\n", end="")
    return (pos)
