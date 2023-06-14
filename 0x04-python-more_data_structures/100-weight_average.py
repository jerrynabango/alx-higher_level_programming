#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        integter1 = 0
        integer2 = 0
        for tup in my_list:
            integter1 += (tup[0] * tup[1])
            integer2 += tup[1]
        return integter1 / integer2
