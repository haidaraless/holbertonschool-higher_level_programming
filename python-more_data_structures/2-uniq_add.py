#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(map(lambda x: x, set(map(lambda i: i, my_list))))
