#!/usr/bin/python3
"""a function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit."""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if posts:
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print("No posts found.")
    elif response.status_code == 404:
        print("Invalid subreddit. Please provide a valid subreddit.")
    else:
        print("Error fetching data from Reddit API.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

