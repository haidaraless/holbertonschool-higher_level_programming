#!/usr/bin/python3
"""
A class that represents Square which is inherits Rectangle class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
    Declaring a Square class
    """

    def __init__(self, size):
        """
        Accepts one arguments (size) to represent Square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """calculates square area"""

        return super().area()
