#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = add_missing_item(tuple_a)
    if len(tuple_b) < 2:
        tuple_b = add_missing_item(tuple_b)

    sum_a = calculate_sum(tuple_a)
    sum_b = calculate_sum(tuple_b)

    return sum_a, sum_b


def add_missing_item(tuple=()):
    new_tuple = tuple
    while len(new_tuple) < 2:
        new_tuple += (0,)
    return new_tuple


def calculate_sum(tuple=()):
    sum = 0
    for i in range(2):
        sum += tuple[i]
    return sum
