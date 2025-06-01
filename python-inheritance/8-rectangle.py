#!/usr/bin/python3
"""
A class that represents Rectangle which is inherits BaseGeometry class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """
    Declaring a Rectangle class
    """

    def __init__(self, width, height):
        """
        Accepts two arguments (width & height) to represent Rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
