#!/usr/bin/python3
"""Query Reddit API for number of subscribers of a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/mellow)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    if not data:
        return 0
    return data.get("subscribers", 0)
