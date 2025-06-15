#!/usr/bin/python3

"""
loads from json file
"""
import json


def load_from_json_file(filename):
    """
    creates an object from json file
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
