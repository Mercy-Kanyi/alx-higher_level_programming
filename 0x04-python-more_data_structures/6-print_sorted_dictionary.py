#!/usr/bin/python3

# prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    #dict_list = a_dictionary.sort
    for i, j in sorted(a_dictionary.items()):
        print(i,': ', j)
