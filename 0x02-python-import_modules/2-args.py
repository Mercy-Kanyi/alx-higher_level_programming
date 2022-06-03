#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = len(sys.argv) - 1

    if (len(sys.argv) == 1):
        print(argv, "arguments.")
    elif (len(sys.argv) == 2):
        print(argv, "argument:")
    else:
        print(argv, "arguments:")

    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
