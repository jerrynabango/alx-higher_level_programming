#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


def it():
    api = sys.argv[1] if len(sys.argv) > 1 else ""
    url = f"http://0.0.0.0:5000/search_user"
    search = requests.post(url, data={"q": api})

    try:
        content = search.json()
        if content == {}:
            print("No result")
        else:
            print("[{}] {}".format(content.get("id"), content.get("name")))
    except Exception:
        print("Not a valid JSON")


if __name__ == '__main__':
    it()
