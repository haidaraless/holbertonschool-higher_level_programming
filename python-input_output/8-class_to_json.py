#!/usr/bin/python3

"""
A function that returns dictionary discription for a json
"""


def class_to_json(obj):
    """
    Returns the dictionary description with data structure
    for json serialization of an object
    """
    return obj.__dict__
