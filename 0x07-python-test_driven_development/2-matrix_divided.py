#!/usr/bin/python3

"""
Divide a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """
    if (not isinstance(matrix, list) or len(matrix) == 0 or
        not all(isinstance(elements, list) for elements in matrix) or
        not all(isinstance(integer, (int, float))
                for integer in [n for elements in matrix for n in elements])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(elements) == len(matrix[0]) for elements in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divide = [list(map(lambda x: round(x / div, 2), elements))
              for elements in matrix]

    return divide
