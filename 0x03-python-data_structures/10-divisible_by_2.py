#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    find = my_list.copy()
    for find_all in range(0, len(my_list)):
        if my_list[find_all] % 2 == 0:
            find[find_all] = True
        else:
            return find
