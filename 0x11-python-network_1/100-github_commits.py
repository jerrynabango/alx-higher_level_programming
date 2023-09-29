#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
"""

import requests
import sys


def time():
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    takes = requests.get(url)
    argument = takes.json()

    try:
        for solve in range(10):
            print("{}: {}".format(
                argument[solve].get("sha"),
                argument[solve].get("commit").get("author").get("name")))
    except IndexError:
        pass


if __name__ == "__main__":
    time()
