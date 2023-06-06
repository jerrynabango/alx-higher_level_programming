#!/usr/bin/python3
for numbers in range(0, 8):
    for digit in range(numbers + 1, 10):
        print("{:d}{:d}".format(numbers, digit), end = ", ")
print("{:d}{:d}".format(numbers + 1, digit))
