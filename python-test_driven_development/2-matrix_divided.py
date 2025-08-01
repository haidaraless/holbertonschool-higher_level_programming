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

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
