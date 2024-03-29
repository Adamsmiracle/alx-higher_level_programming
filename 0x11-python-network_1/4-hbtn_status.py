#!/usr/bin/python3
"""Makes a GET request to the url"""

import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
