#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r") as file:  # "r" is used for reading from stdin and writing to stdout
        print(file.read(), end="\n")