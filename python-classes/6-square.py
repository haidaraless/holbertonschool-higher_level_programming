#!/usr/bin/python3
"""Declare a class Square"""


class Square:
    """a class to represent Square"""

    def __init__(self, size=0, position=(0, 0)):
        """an instance variable to accept the size with validating input"""

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """a property to get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """a property to set position"""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """print a square using hash symbol"""
        if self.size == 0:
            print("")

        print("\n" * self.position[1], end="")
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
