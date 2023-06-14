#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for uniq_integer in set(my_list):
        sum += uniq_integer
    return sum
