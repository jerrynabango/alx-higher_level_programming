#!/usr/bin/python3
def remove_char_at(str, n):
    character = 0
    copy = ""
    for chr in str:
        if character != n:
            copy += chr
        character += 1
    return copy
