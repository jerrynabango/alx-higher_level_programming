#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable.
"""

import urllib.request
import sys


def takes_url():
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        print(response.info().get('X-Request-Id'))


if __name__ == '__main__':
    takes_url()
