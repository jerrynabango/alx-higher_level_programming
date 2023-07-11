#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, "w") as file:  # "w" is used for writing to a file
        return file.write(text)
