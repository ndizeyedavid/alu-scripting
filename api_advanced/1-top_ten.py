#!/usr/bin/python3
"""Query Reddit API for top ten hot posts of a subreddit."""

import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}
    params = {"limit": 10}
    try:
        res = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
        posts = res.json().get("data").get("children")
        for post in posts[:10]:
            print(post.get("data").get("title"))
    except Exception:
        print(None)
