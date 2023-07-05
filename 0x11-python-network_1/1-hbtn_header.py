#!/usr/bin/python3
"""
Module to send a request to a URL and display the value of the X-Request-Id header variable.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.info()

    x_request_id = headers.get('X-Request-Id')
    print(x_request_id)
