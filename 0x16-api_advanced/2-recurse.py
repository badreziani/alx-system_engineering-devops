#!/usr/bin/python3
"""
    Uses Reddit API to get all hot posts
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Get all hot posts"""
    if after is None:
        return []

    url = 'https://www.reddit.com/r/{}/hot.json?limit=100&after={}'.format(
            subreddit, after)
    headers = {'user-agent': 'fakeuser'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return None

        json = response.json()
        posts = json.get("data").get("children")

        for post in posts:
            hot_list.append(post.get("data").get("title"))
        return hot_list + recurse(subreddit, [], json.get("data").get("after"))
    except Exception:
        return None
