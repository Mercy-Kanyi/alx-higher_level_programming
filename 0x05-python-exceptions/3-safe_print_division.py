#!/usr/bin/python3

# a function that divides 2 integers and prints the result
def safe_print_division(a, b):
    try:
        quo = a / b
    except ZeroDivisionError:
        quo = None
    finally:
        print("Insise result: {}".format(quo))
        return quo
