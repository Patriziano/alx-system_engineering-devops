#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit, the
    function should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Using recursion"""
    apiUrl = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'MyBot/1.0'}
    params = {'after': after} if after else {}

    res = requests.get(apiUrl, headers=headers, params=params)

    if res.status_code == 200:
        data = res.json()
        posts = data['data']['children']
        after = data['data']['after']

        if not posts:
            if not hot_list:
                return None
            else:
                return hot_list

        hot_list.extend([post['data']['title'] for post in posts])

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
