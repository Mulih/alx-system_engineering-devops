#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
