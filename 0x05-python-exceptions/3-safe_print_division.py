#!/usr/bin/python3

# a function that divides 2 integers and prints the result
def safe_print_division(a, b):
    try:
        var = a / b
    except ZeroDivisionError:
        var = None
    finally:
        print("Inside result: {}".format(var))
    return var
