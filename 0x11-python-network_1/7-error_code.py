#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""

import requests
import sys


def error():
    url = sys.argv[1]
    errors = requests.get(url)
    if errors.status_code >= 400:
        print("Error code: {}".format(errors.status_code))
    else:
        print(errors.text)


if __name__ == "__main__":
    error()
