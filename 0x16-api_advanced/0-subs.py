#!/usr/bin/python3
"""use Reddit API and returnsthe number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except requests.RequestException as e:
        return 0
    except KeyError:
        return 0

