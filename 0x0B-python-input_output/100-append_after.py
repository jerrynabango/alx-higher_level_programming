#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file, after each line
    containing a specific string
    """
    with open(filename, "r") as file:
        line = file.readline()
        new_line = ""
        while line:
            new_line += line
            if search_string in line:
                new_line += new_string
            line = file.readline()

    with open(filename, "w") as file:
        file.write(new_line)
