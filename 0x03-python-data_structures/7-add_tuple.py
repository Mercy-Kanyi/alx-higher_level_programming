#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # create a new tuple
    sum_tuple = ()
    # convert tuples a and b into tuples with two elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    # add the elemnts of the tuples
    sum_tuple = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    return sum_tuple
