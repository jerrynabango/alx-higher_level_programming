#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_del = []
    for keys in a_dictionary:
        if a_dictionary[keys] == value:
            keys_to_del.append(keys)
    for keys in keys_to_del:
        del a_dictionary[keys]
    return a_dictionary
