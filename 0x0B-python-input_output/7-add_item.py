#!/usr/bin/python3
""" Load, add, save arguments"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
"""save to json file name and arguments from save_to_json function"""

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
"""load from json file from json file path"""

filename = "add_item.json"
"""save to json file name for loading from json file"""


def script(argv):
    """
    script that adds all arguments to a Python list,
    and then save them to a file
    """


try:
    json_list = load_from_json_file(filename)
except FileNotFoundError:
    json_list = []
for arg in argv[1:]:
    json_list.append(arg)
save_to_json_file(json_list, filename)
