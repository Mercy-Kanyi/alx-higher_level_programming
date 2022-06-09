#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
<<<<<<< HEAD
    for row in matrix:
        print(" ".join("{:d}".format(q) for q in row))
=======
    # move through each line of the matrix given
    for line in matrix:
        # define a separator that you'd like to use
        d = " "
        # use the 'generator expression' method together with join
        print(d.join(("{:d}".format(i)) for i in line))
>>>>>>> c24c739258e1fa19ffb59c4b1bb388f18a4b110e
