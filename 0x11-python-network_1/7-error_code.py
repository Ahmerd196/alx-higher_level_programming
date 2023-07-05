#!/usr/bin/python3
"""
Module to send a request to a URL and display the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    body = response.text

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(body)
