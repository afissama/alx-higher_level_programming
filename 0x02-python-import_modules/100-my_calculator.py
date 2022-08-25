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
        print(ops[op](a, b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
