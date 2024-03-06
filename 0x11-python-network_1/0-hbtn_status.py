#!/usr/bin/python3
"""
script that hat fetches https://alx-intranet.hbtn.io/status

    You must use the package urllib
"""

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        response = response.read()
        print("Response body:")
        print(f"\t- type: {type(response)}")
        print(f"\t- content: {response}")
        print(f"\t- utf8 content: {response.decode('utf-8')}")
