#!/usr/bin/python3

"""
A class that represents Student
"""


class Student:
    """
    Define Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Constructor of Student class that accepts
        first and last name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation
        """
        if attrs is None:
            return self.__dict__
        result = {}

        for attr_name in attrs:
            if attr_name == "age":
                result["age"] = self.age
            elif attr_name == "first_name":
                result["first_name"] = self.first_name
            elif attr_name == "last_name":
                result["last_name"] = self.last_name
        return result
