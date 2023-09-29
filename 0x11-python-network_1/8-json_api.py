#!/usr/bin/python3

"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


def letter():
    leta = sys.argv[1] if len(sys.argv) > 1 else ""
    url = f'http://0.0.0.0:5000/search_user'
    post_request = requests.post(url, data={'leta': leta})

    try:
        content = post_request.json()
        if content == {}:
            print("No result")
        else:
            print("[{}] {}".format(content.get('id'), content.get('name')))
    except Exception:
        print('Not a valid JSON')


if __name__ == '__main__':
    letter()
