#!/usr/bin/python3
# 101-lazy_matrix_mul.py
""" Lazy matrix multiplication"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies two matrices"""
    return (np.matmul(m_a, m_b))