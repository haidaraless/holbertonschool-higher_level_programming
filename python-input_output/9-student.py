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

    def to_json(self):
        """
        retrieves a dictionary representation
        """
        return self.__dict__
