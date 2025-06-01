#!/usr/bin/python3
"""
Checks if an object is inherits from a given class
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is inherits from a_class
    otherwise returns False
    """

    return issubclass(type(obj), a_class)
