#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    safe_list = 0
    list = 0
    while list < x:
        try:
            print(my_list[list], end="")
            safe_list += 1
            list += 1
        except IndexError:
            break
    print()
    return (safe_list)
