#!/usr/bin/python3

"""
A Find a peak
"""


def find_peak(list_of_integers):
    """
     Defines the peak of a list of Integers
    """
    if list_of_integers != []:
        peak_1, peak_2 = 0, len(list_of_integers) - 1
        for _ in range(len(list_of_integers)):
            ls = peak_1 + (peak_2 - peak_1) // 2
            if list_of_integers[ls] < list_of_integers[ls + 1]:
                peak_1 = ls + 1
            else:
                peak_2 = ls

        return list_of_integers[peak_1]
