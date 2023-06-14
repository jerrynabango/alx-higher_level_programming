#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        dem = 0
        num = 0
        for tup in my_list:
            dem += (tup[0] * tup[1])
            num += tup[1]
        return dem / num
