#!/usr/bin/python3

"""
writes a string into file content
"""


def write_file(filename="", text=""):
    """
    writes a text into file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
