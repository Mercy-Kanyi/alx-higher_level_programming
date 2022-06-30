#!/usr/bin/python3
"""defines a square with a size"""


class Square:
    """defines a square with a size"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes a sqaure with an optional size
        args: size=0:size of the square position:=(0, 0)
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of square
        args: value: value from user
        """
        if not(isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieves position instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position from the user"""
        if (type(position) is not tuple or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square with the character #,
        at the position given by the position attribute.
        """
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
