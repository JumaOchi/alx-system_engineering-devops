#!/usr/bin/python3
"""
Write a Python script that queries the Reddit API and returns the top ten hot
posts in a subreddit
"""
import json
# import pprint
import requests
import sys

headers = {
    'User-Agent': 'My User Agent 1.0'
}


def top_ten(subreddit):
    """function that returns the titles of the first 10 hot posts"""
    try:
        url = 'https://www.reddit.com/r/'
        response = requests.get(url + subreddit + "/hot.json?limit=10",
                                headers=headers, allow_redirects=False)
        myArray = [element['data']['title'] for element in response.
                   json()['data']['children']]
        print(*myArray, sep='\n')
        # pprint.pprint(response.json())
    except:
        print(None)
