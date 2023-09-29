#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""


def fetches():
    import requests
    fetch_url = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}".
          format(type(fetch_url.text), fetch_url.text))


if __name__ == '__main__':
    fetches()
