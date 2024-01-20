#!/usr/bin/python3
"""a function that queries the Reddit API and returns the
    number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0."""
import requests


def number_of_subscribers(subreddit):
    """to get number of subscribers"""
    apiUrl = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'MyBot/1.0'}
    res = requests.get(apiUrl, headers=headers)

    if res.status_code == 200:
        data = res.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
