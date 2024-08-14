#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ Reddit API Queries  """
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    data_dict = res.json()
    if 'data' not in data_dict:
        return 0
    if 'subscribers' not in data_dict.get('data'):
        return 0
    return res.json()['data']['subscribers']
