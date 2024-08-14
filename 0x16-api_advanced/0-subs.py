#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """ show number of subs for subreddit"""
    if type(subreddit) is not str or subreddit is None:
        return 0
    try:
        headers = {'User-Agent': 'DanielleBadobre'}
        request = requests.get('https://api.reddit.com/r/{}/about'.
                               format(subreddit), headers=headers)
        subscribers = request.json()
        sub = subscribers['data']['subscribers']
        return sub
    except Exception:
        return 0
