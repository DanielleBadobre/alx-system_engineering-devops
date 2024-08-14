#!/usr/bin/python3
"""2-recurse"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """return list of all hot articles from subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            if not children:
                return hot_list if hot_list else None

            hot_list.extend([post['data']['title'] for post in children])
            after = data['data']['after']

            if after is None:
                return hot_list
            else:
                return recurse(subreddit, hot_list, after)
        else:
            return None
    except requests.RequestException:
        return None
