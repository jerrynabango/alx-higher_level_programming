#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the body of the decoded in utf-8.
"""

import urllib.request
import urllib
import sys


def sends():
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    sends()
