#!/usr/bin/python3
"""Query Reddit API for top ten hot posts of a subreddit."""

import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/mellow)"}
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=True
    )
    if response.status_code != 200:
        print("OK")
        return
    data = response.json().get("data", {})
    children = data.get("children", [])
    if not children:
        print(None)
        return
    for child in children[:10]:
        print(child.get("data", {}).get("title"))

if __name__ == "__main__":
    top_ten("programming")
