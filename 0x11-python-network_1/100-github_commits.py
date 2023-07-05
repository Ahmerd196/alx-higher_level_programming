#!/usr/bin/python3
"""
Python script to list 10 commits of a GitHub repository.
"""

import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)

    try:
        response.raise_for_status()
        commits = response.json()

        for commit in commits[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    except requests.exceptions.HTTPError as error:
        print(f"Error: {error.response.status_code}")
    except (KeyError, ValueError):
        print("Invalid response from the GitHub API")
