#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) != 0:
        largest = my_list[0]
        for i in my_list:
            if i > largest:
                largest = i
        return largest
    return None
# or you could use .sort function as well
