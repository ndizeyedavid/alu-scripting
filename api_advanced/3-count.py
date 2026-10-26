#!/usr/bin/python3
"""Recursively query Reddit and count keyword occurrences in hot titles."""

import re

import requests


def count_words(subreddit, word_list, hot_list=None, after=None):
    """Print sorted counts of keywords in hot article titles."""
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
        return

    data = response.json().get("data", {})
    children = data.get("children", [])
    if not children and not hot_list and after is None:
        return

    for child in children:
        title = child.get("data", {}).get("title")
        if title:
            hot_list.append(title)

    next_after = data.get("after")
    if next_after:
        count_words(subreddit, word_list, hot_list, next_after)
        return

    lowered_words = [w.lower() for w in word_list]

    agg = {}
    for word in lowered_words:
        agg[word] = agg.get(word, 0)
    for title in hot_list:
        title_lower = title.lower()
        for word in lowered_words:
            pattern = r"\b" + re.escape(word) + r"\b"
            agg[word] += len(re.findall(pattern, title_lower))

    result = []
    for word, count in agg.items():
        if count > 0:
            result.append((word, count))

    result.sort(key=lambda x: (-x[1], x[0]))
    for word, count in result:
        print("{}: {}".format(word, count))
