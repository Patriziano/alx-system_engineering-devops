#!/usr/bin/python3
""" a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if not word_list:
        print_results(counts)
        return

    word = word_list[0].lower()
    rest_of_words = word_list[1:]

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts:
            title = post['data']['title'].lower()
            counts[word] = counts.get(word, 0) + title.count(word)

        after = data.get('data', {}).get('after')
        count_words(subreddit, rest_of_words, after, counts)
    elif response.status_code == 404:
        print("Invalid subreddit. Please provide a valid subreddit.")
    else:
        print("Error fetching data from Reddit API.")

def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")
