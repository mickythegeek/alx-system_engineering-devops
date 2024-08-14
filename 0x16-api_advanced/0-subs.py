#!/usr/bin/python3
import requests
import sys

def number_of_subscribers(subreddit):
    user_agent = 'Mozilla/5.0'
    
    headers = {
        'User-Agent': user_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    if 'd' not in data:
        return 0
    if 'subscribers' not in data.get('d'):
        return 0
    return response.json()['d']['subscribers']
