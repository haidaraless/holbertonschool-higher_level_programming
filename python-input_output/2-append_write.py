#!/usr/bin/python3

"""
appends text at the end of a file
"""


def append_write(filename="", text=""):
    """
    appends text at the end of the given file
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
