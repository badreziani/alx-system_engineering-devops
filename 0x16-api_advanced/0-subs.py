#!/usr/bin/python3
"""0-subs module
contains the definiton of number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers
    queries the Reddit API and returns the number of subscribers
    If not a valid subreddit, return 0."""

    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        headers = {'user-agent': 'fakeuser'}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return 0

        return response.json().get("data").get("subscribers")
    except Exception:
        return 0
