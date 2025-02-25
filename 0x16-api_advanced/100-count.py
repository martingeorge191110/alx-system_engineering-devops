#!/usr/bin/python3
"""recursive function that queries the Reddit API,
parses the title of all hot articles"""
import requests


def count_words(subreddit, word_list, words={}, after=None):
    apiUrl = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    if words == {}:
        for word in word_list:
            words[word] = 0

    res = requests.get(apiUrl, headers={
        "User-Agent": "Mozilla/5.0"
    }, allow_redirects=False)

    if res.status_code == 200:
        dataObj = res.json().get("data")
        after = dataObj.get("after")

        for ele in dataObj.get("children"):
            for title in ele.get("data").get("title").split():
                if title.lower() in word_list:
                    words[title.lower()] += 1

        if after is None:
            newWordList = sorted(words)
            for ele in newWordList:
                if words[ele] != 0:
                    print(f"{ele}: {words[ele]}")
        return (count_words(subreddit, word_list, words, after))
    else:
        pass
