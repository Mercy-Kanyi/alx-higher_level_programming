#!/usr/bin/python3

import sys

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if len(sys.argv) == 4:
        a, op, b = sys.argv[1:]
        if sys.argv[2] == "+":
            print("{} {} {} = {}".format(a, op, b, add(int(a), int(b))))
        elif sys.argv[2] == "-":
            print("{} {} {} = {}".format(a, op, b, sub(int(a), int(b))))
        elif sys.argv[2] == "*":
            print("{} {} {} = {}".format(a, op, b, mul(int(a), int(b))))
        elif sys.argv[2] == "/":
            print("{} {} {} = {}".format(a, op, b, div(int(a), int(b))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
