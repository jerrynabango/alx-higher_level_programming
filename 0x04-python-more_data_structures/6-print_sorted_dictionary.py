#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ordered_keys in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(ordered_keys, a_dictionary[ordered_keys]))
