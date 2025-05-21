#!/usr/bin/python3
"""declare a class attribute (variable) to return size"""


class Square:
    __size = 0

    def __init__(self, size):
        """an instance variable to accept the size"""
        self.__size = size
