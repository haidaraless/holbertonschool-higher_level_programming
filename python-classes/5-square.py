#!/usr/bin/python3
"""declare a private class attribute (variable) to return size"""


class Square:
    """a class to represent Square"""
    __size = 0

    def __init__(self, size=0):
        """an instance variable to accept the size with validating input"""

        self.__size = size

    def area(self):
        """a public method that calculates area of square"""
        return self.__size**2

    @property
    def size(self):
        """a property to get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """a property to set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """print a square using hash symbol"""
        if self.size == 0:
            print()

        for c in range(self.size):
            for r in range(self.size):
                print("#", end="")
            print()
