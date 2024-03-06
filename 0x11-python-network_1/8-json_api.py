#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argc[1]
    else:
        q = ""
    data = {'q': q}
    res = requests.post(url, data=data)
    try:
        jsonres = res.json()
        if jsonres:
            print(f"[{jsonres.get('id')}] {jsonres.get('name')}")
        else:
            print("No results")

    except ValueError:
        print("not a valid JSON")
