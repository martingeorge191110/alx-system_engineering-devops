#!/usr/bin/python3
"""function that queries the Reddit API, returns
the number of subscribers for a given subreddit"""
import json
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    apiData = requests.get(f"{url}", headers={
        "User-Agent": "Mozilla/5.0"
    }).text

    data = json.loads(apiData)

    if data.get("error") == 404:
        return (0)
    else:
        return (data.get("data").get("subscribers"))
