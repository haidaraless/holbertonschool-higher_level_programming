#!/usr/bin/python3

"""
saves json content into file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    saves a json content into a json file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
