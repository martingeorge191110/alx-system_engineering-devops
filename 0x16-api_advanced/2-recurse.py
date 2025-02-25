#!/usr/bin/python3
"""recursive function that queries the Reddit API,
returns a list containing the titles
of all hot articlesfor a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    res = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0"
    }, allow_redirects=False)

    if res.status_code != 200:
        return (None)
    else:
        data = res.json().get("data")
        after = data.get("after")

        for ele in data.get("children"):
            hot_list.append(ele.get("data").get("title"))

        if not after:
            return hot_list
        return (recurse(subreddit, hot_list, after))
