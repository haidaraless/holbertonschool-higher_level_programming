#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    return reduce(lambda a, b: a+b, set(my_list))
