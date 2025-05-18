#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    exists = key in a_dictionary
    if exists:
        del a_dictionary[key]
    return a_dictionary
