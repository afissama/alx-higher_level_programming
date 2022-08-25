#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argv = sys.argv
    if len(argv) != 4:
        print("/100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if op in ops.keys():
        print("{} {} {} = {}".format(a, op, b, ops[op](a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
