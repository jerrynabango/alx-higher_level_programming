#!/usr/bin/python3
"""Matrix multiplication"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    list_1 = 0
    mat = 0

    if m_a == []:
        raise ValueError("m_a can't be empty")
    for mat_1 in m_a:
        if type(mat_1) != list:
            raise TypeError("m_a must be a list of lists")
        size_1 = len(m_a[0])
        if mat_1 == []:
            raise ValueError("m_a can't be empty")
        if size_1 != len(mat_1):
            raise TypeError("each row of m_a must be of the same size")
        list_1 = len(mat_1)
        for list_2 in mat_1:
            if type(list_2) != int and type(list_2) != float:
                raise TypeError("m_a should contain only integers or floats")

    if m_b == []:
        raise ValueError("m_b can't be empty")
    for mat_2 in m_b:
        if type(mat_2) != list:
            raise TypeError("m_b must be a list of lists")
        size_2 = len(m_b[0])
        if mat_2 == []:
            raise ValueError("m_b can't be empty")
        if size_2 != len(mat_2):
            raise TypeError("each row of m_b must be of the same size")
        mat += 1
        for list_3 in mat_2:
            if type(list_3) != int and type(list_3) != float:
                raise TypeError("m_b should contain only integers or floats")

    if list_1 != mat:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []

    mat_2_index = 0
    while mat_2_index < len(m_a):
        mat_2 = m_a[mat_2_index]
        matrx = 0
        mat_4 = []
        while matrx < len(m_b[0]):
            result = 0
            matri_multi = 0
            mat_5_index = 0
            while mat_5_index < len(mat_2):
                mat_5 = mat_2[mat_5_index]
                result += mat_5 * m_b[matri_multi][matrx]
                matri_multi += 1
                mat_5_index += 1
            mat_4.append(result)
            matrx += 1
        mul_matrix.append(mat_4)
        mat_2_index += 1

    return mul_matrix
