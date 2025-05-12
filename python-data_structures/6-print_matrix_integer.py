#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for e in range(len(matrix[i])):
            print("{:d}".format(matrix[i][e]), end="")
            if e < len(matrix[i]) - 1:
                print(" ", end="")
        print()
