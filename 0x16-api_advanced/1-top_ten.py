#!/usr/bin/python3
"""function that queries the Reddit API, prints
the titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    api = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    res = requests.get(f"{api}", headers={
        "User-Agent": "Mozilla/5.0"
    }, allow_redirects=False)

    if res.status_code != 200:
        print("None")
    else:
        data = res.json().get("data")
        hottestPosts = data.get("children")

        for ele in hottestPosts:
            print(ele.get("data").get("title"))
