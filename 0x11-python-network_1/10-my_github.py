#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import sys
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]

    res = requests.get(url, auth=(username, token))
    jsonres = res.json()
    print(jsonres.get("id"))
