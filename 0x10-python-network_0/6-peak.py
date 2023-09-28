#!/usr/bin/python3
"""
Find a peak
"""


def find_peak(list_of_integers):
    """
    Defines the peak function for a list of Integers
    """
    if list_of_integers != []:
        peak_1, peak_2 = 0, len(list_of_integers) - 1
        for _ in range(len(list_of_integers)):
            mid = peak_1 + (peak_2 - peak_1) // 2
            if list_of_integers[mid] < list_of_integers[mid + 1]:
                peak_1 = mid + 1
            else:
                peak_2 = mid
        return list_of_integers[peak_1]
