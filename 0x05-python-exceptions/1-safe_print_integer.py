#!/usr/bin/python3

# a function that prints an integer with "{:d}".format()
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError as ex:
        return False
