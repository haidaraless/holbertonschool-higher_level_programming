#!/usr/bin/python3

"""
returns a json representation of a given object
"""
import json


def to_json_string(my_obj):
    """
    returns json representation of my_obj
    """
    return json.dumps(my_obj)
