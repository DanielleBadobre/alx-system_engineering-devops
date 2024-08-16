#!/usr/bin/python3
""" 100-recurse """
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_count=None):
    """Print a sorted count of given keywords from hot article titles."""
    if word_count is None:
        word_count = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        children = data['data']['children']
        after = data['data']['after']

        normalized_word_list = [word.lower() for word in word_list]

        for post in children:
            title_words = post['data']['title'].lower().split()
            for word in normalized_word_list:
                word_count[word] += title_words.count(word)

        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_word_count = sorted(
                [(word, count) for word, count in word_count.items()
                    if count > 0],
                key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
    except requests.RequestException:
        return
