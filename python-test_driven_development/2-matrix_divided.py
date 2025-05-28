#!/usr/bin/python3

"""
A module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    calclates the division of each item of a row within a matrix
    """

    validate_inputs(matrix, div)

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]


def validate_inputs(matrix, div):
    """
    validates matrix and division number
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix\
        (list of lists) of integers/floats")

    for r in range(len(matrix)):
        if not isinstance(matrix[r], list):
            raise TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
