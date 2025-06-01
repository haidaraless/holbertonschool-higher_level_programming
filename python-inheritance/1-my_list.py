#!/usr/bin/python3
"""
Inherit MyList from the original (built-in) list
"""


class MyList(list):

    """
    prints sorted list (ascending sort)
    """
    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
