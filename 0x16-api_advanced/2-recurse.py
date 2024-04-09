#!/usr/bin/python3
"""
script to query list of all hot posts on a particular Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    
    # create URL for subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # define headers for HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # define parameters for request, including pagination and limit
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # send a GET request to subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # check if response status code indicates a not-found error (404)
    if response.status_code == 404:
        return None
    # parse JSON response and extract relevant data
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    # append post titles to hot_list
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    # if there exist more posts to retrieve, recursively call the function
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # return final list of hot post titles
    return hot_list
