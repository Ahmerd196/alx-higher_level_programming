#!/usr/bin/python3
"""
Module to display the user id using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    try:
        response.raise_for_status()
        user_data = response.json()
        user_id = user_data["id"]
        print("User ID: {}".format(user_id))
    except requests.exceptions.HTTPError as error:
        print("Error: {}".format(error.response.status_code))
    except (KeyError, ValueError):
        print("Invalid response from the GitHub API")
