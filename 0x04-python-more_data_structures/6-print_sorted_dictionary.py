#!/usr/bin/python3

# prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    for i, j in sorted(a_dictionary.items()):
        print("{}: {}".format(i, j))
