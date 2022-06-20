#!/usr/bin/python3

# a function that divides 2 integers and prints the result
def safe_print_division(a, b):
    try:
        quo = a / b
        return quo
    except ZeroDivisionError:
        quo = None
        return quo
    finally:
        print("Insise result: {}".format(quo))

