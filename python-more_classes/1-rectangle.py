#!/usr/bin/python3
"""A class that represents Rectangle"""


class Rectangle:
    """Defines rectangle with width and height"""

    def __init__(self, width=0, height=0):
        """an initilizer of Rectangle object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """a getter of width attribute"""
        return self.__width

    @property
    def height(self):
        """a getter of height attribute"""
        return self.__height

    @width.setter
    def width(self, value):
        """a setter of width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """a setter of height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
