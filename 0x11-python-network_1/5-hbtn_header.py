#!/usr/bin/python3
"""
Module to fetch a URL and display the value of the X-Request-Id variable in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    headers = response.headers
    x_request_id = headers.get('X-Request-Id')

    print(x_request_id)
