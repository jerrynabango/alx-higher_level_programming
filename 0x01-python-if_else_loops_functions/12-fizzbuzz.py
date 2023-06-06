#!/usr/bin/env python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3*5 == 0:
            print("Fizzbuzz", end = " ")
        elif number % 3 == 0:
            print("Fizzbuzz", end = " ")
        elif number % 5 == 0:
            print("Fizzbuzz", end = " ")
        else:
            print("{:d}".format(number), end = " ")