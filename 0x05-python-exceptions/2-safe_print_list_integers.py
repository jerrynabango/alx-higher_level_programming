#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    list = 0
    for print_list in range(x):
        try:
            print("{:d}".format(my_list[print_list]), end="")
            list += 1
        except (ValueError, TypeError):
            continue
    print()
    return list
