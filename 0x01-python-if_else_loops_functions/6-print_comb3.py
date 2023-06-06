#!/usr/bin/python3
for numbers in range(8):
    for digit in range(numbers + 1, 10):
        print("{:d}{:d}".format(numbers, digit), end = ", ")
print("{:d}{:d}".format(numbers + 1, digit))#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")
