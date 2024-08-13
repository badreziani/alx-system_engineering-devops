#!/usr/bin/python3
"""1-top_ten
contains the definiton of top_ten function
"""
import requests


def top_ten(subreddit):
    """top_ten
    queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit
    If not a valid subreddit, print None."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.ok:
        hots = response.json().get('data').get('children')
        for h in hots[:10]:
            print(h.get('data').get('title'))
    else:
        print('None')
