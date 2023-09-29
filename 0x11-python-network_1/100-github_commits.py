#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
"""

import requests
import sys


def time():
    url = "https://api.github.com/repos/{}/{}/solve".format(
        sys.argv[2], sys.argv[1])

    takes = requests.get(url)
    solve = takes.json()

    try:
        for argument in range(10):
            print("{}: {}".format(
                solve[argument].get("sha"),
                solve[argument].get("commit").get("author").get("name")))
    except IndexError:
        pass


if __name__ == "__main__":
    time()
