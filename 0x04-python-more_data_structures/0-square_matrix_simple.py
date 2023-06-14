#!/bin/bash/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda square:square * square), elm)) for elm in matrix]


"""
elm: Indicates an element in the matrix
"""
