#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the
    Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        integer_1 = triangle[-1]
        integer_2 = [1]
        size = 0

        while size < len(integer_1) - 1:
            integer_2.append(integer_1[size] + integer_1[size + 1])
            size += 1

        integer_2.append(1)
        triangle.append(integer_2)

    return triangle
