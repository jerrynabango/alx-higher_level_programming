#!/usr/bin/python3
def no_c(my_string):
    remove = ""
    for characters in my_string:
        if characters != "C" and characters != "c":
            remove += characters
    return remove