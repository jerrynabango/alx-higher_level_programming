#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    biggest_integer = my_list[0]
    for integer in range(1, len(my_list)):
        if biggest_integer < my_list[integer]:
            biggest_integer = my_list[integer]
        else:
            continue

    return biggest_integer
