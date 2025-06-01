#!/usr/bin/python3
"""
Checks if an object is belongs to given class
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is instance of a_class otherwise returns False
    """

    if type(obj) is a_class:
        return True
    else:
        return False