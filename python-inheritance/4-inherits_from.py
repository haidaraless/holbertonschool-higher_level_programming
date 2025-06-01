#!/usr/bin/python3
"""
Checks if an object's class is inherits from a given class
directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    Return True if object's class is inherits from a_class
    directly or indirectly otherwise returns False
    """

    return not type(obj) is a_class and issubclass(type(obj), a_class)
