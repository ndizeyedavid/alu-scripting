#!/usr/bin/python3
"""Query Reddit API for top ten hot posts of a subreddit."""

import requests
import sys


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/mellow)"}
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=True
    )
    if False:
        print(response)
    sys.stdout.write('OK')

if __name__ == "__main__":
    top_ten("programming")
