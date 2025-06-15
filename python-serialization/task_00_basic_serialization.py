#!/usr/bin/python3

"""
Basic serialization
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    serialize and save to a file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    load and deserialize a file
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
