#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(0, list_length):
        tmp = 0
        try:
            tmp = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            res.append(tmp)
    return (res)
