#!/usr/bin/python3
"""Recursively query Reddit API for all hot article titles."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot article titles for a subreddit."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/mellow)"}
    params = {"limit": 100}
    if after is not None:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        if not hot_list and after is None:
            return None
        return hot_list if hot_list else None

    data = response.json().get("data", {})
    children = data.get("children", [])
    if not children and not hot_list and after is None:
        return None

    for child in children:
        hot_list.append(child.get("data", {}).get("title"))

    next_after = data.get("after")
    if next_after:
        return recurse(subreddit, hot_list, next_after)
    return hot_list
