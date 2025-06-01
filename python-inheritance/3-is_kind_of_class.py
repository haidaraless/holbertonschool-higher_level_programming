#!/usr/bin/python3
"""
Checks if an object is belongs or inherit of a given class
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is instance or inherit from a_class
    otherwise returns False
    """

    return isinstance(obj, a_class)
