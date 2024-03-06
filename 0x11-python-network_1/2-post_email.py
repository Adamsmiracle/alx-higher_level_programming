#!/usr/bin/python3
"""
 script that takes in a URL and an email, sends a POST 
 request to the passed URL with the email as a parameter, 
 and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {"email": email}
    data = urllib.parse.urlencode(param)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as res:
        print(res.read().decode('utf-8'))
