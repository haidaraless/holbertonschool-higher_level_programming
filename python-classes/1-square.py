#!/usr/bin/python3
"""declare a private class attribute (variable) to return size"""


class Square:
    """a class to represent Square"""
    __size = 0

    def __init__(self, size):
        """an instance variable to accept the size"""
        self.__size = size
