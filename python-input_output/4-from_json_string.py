#!/usr/bin/python3

"""
converts a json string into an object
"""
import json


def from_json_string(my_str):
    """
    converts a json string into an object (data structure)
    """
    return json.loads(my_str)
