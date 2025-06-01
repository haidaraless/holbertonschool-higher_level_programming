#!/usr/bin/python3
"""
An empty class that represents BaseGeometry
"""


class BaseGeometry:
    """
    Empty class with pass until fill its behavoir and attributes
    """

    def area(self):
        """
        An empty method that should be used to calculates the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            validates input value
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
