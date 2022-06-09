#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    # move through each line of the matrix given
    for line in matrix:
        # define a separator that you'd like to use
        d = " "
        # use the 'generator expression' method together with join
        print(d.join(("{:d}".format(i)) for i in line))
