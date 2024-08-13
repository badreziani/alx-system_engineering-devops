#!/usr/bin/python3
"""0-subs module
contains the definiton of number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """number_of_subscribers
    queries the Reddit API and returns the number of subscribers
    If not a valid subreddit, return 0."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url)
    if response.ok:
        return response.json().get('data').get('subscribers')
    else:
        return 0
