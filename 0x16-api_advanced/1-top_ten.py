#!/usr/bin/python3
"""a function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """This function gets first 10 comments"""
    apiUrl = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {'User-Agent': 'MyBot/1.0'}
    res = requests.get(apiUrl, headers=headers)

    if res.status_code == 200:
        data = res.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print('None')
