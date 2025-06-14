#!/usr/bin/python3
"""
Declaring a function that reads a file and print its content
"""


def read_file(filename=""):
    """
    reads file's content and print it out
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
