#!/usr/bin/python3
"""
accepts url and sends request to the url
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        value = response.getheader("X-Request-id")
        print(value)
