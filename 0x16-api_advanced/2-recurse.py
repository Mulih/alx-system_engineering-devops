#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API for hot articles in a given subreddit.
    Returns a list of article titles or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {"limit": 100}  # Maximum number of items per request
    if after:
        params["after"] = after

    data = response.json()
    if "data" in data and "children" in data["data"]:
        for child in data["data"]["children"]:
            hot_list.append(child["data"]["title"])
        # Check if there are more pages
        if "after" in data["data"]:
            return recurse(subreddit, hot_list, data["data"]["after"])
        else:
            return hot_list
    else:
        return None
