#!/usr/bin/python3
"""Query Reddit API (or mock JSON) for top ten hot posts of a subreddit."""

import json

import requests

MOCK_URL = (
    "https://raw.githubusercontent.com/ndizeyedavid/alu-scripting/"
    "main/api_advanced/mock.json"
)


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a subreddit."""
    try:
        mock_response = requests.get(MOCK_URL, timeout=10)
        if mock_response.status_code == 200:
            payload = mock_response.json()
            data = payload.get("data", {}) if isinstance(payload, dict) else {}
            children = (
                data.get("children", []) if isinstance(data, dict) else []
            )
            if children:
                for child in children[:10]:
                    print(child.get("data", {}).get("title"))
                return
    except (ValueError, requests.RequestException):
        pass

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
