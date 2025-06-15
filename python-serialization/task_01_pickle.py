#!/usr/bin/python3
"""
custom class serialization using pickle module
"""
import pickle


class CustomObject:
    """
    custom class for demonstrating pickle serialization
    """

    def __init__(self, name, age, is_student):
        """
        initialize CustomObject instance
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        display the object's attributes in the specified format
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        serialize the current instance and save it to a file
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize an object from a file and return the instance
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
