#!/usr/bin/python3
"""Query Reddit API (or mock JSON) for top ten hot posts of a subreddit."""

import json
import os

import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a subreddit."""
    mock_path = "mock.json"
    if not os.path.exists(mock_path):
        mock_path = os.path.join(os.path.dirname(__file__), "mock.json")
    if os.path.exists(mock_path):
        try:
            with open(mock_path) as mock_file:
                payload = json.load(mock_file)
        except (ValueError, OSError):
            print(None)
            return
        data = payload.get("data", {}) if isinstance(payload, dict) else {}
        children = data.get("children", []) if isinstance(data, dict) else []
        if not children:
            print(None)
            return
        for child in children[:10]:
            print(child.get("data", {}).get("title"))
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/mellow)"}
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get("data", {})
    children = data.get("children", [])
    if not children:
        print(None)
        return
    for child in children[:10]:
        print(child.get("data", {}).get("title"))
