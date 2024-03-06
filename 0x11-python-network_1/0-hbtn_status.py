#!/usr/bin/python3
"""
script that hat fetches https://alx-intranet.hbtn.io/status

    You must use the package urllib
"""

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        request = response.read()
        print("Response body")
        print(f"\t- type: {type(res)}")
        print(f"\t- content: {res}")
        print(f"\t- utf8 content: {res.decode('utf-8')}")
