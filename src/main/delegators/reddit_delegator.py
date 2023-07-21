'''
reddit_delegator.py

Interacts with the Reddit API to request and retrieve data.
'''

import praw
from praw.models.reddit.subreddit import ContributorRelationship
from praw.reddit import Reddit

class RedditDelegator:

    def __init__(self, **configs):
        reddit = praw.Reddit(
            client_id=configs["client_id"],
            client_secret=configs["client_secret"],
            password=configs["user_password"],
            user_agent=configs["user_agent"],
            username=configs["username"],
        )


    def get_recent_posts(self, num_posts: int) -> list:
        return list()
