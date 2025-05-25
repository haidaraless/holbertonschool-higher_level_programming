#!/usr/bin/python3
"""A class that represents Rectangle"""


class Rectangle:
    """Defines rectangle with width and height"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """an initilizer of Rectangle object"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """caluculates area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """caluculates perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """prints rectangle based on its width and height"""
        if self.height == 0 or self.width == 0:
            return ""

        rec = []
        for h in range(self.height):
            rec.append("#" * self.width)
        return "\n".join(rec)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
