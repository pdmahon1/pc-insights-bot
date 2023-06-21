'''
reddit_delegator.py

Interacts with the Reddit API to request and retrieve data.
'''

from praw.models.reddit.subreddit import ContributorRelationship
from praw.reddit import Reddit
import os


class RedditDelegator:
    def is_valid_credentials(self, credentials: dict) -> bool:
        return True

    @staticmethod    
    def get_reddit_object(self, credentials: dict) -> Reddit:
        if is_valid_credentials(credentials):
            return praw.Reddit(
                client_id = credentials["client"]["username"],
                client_secret = credentials["client"]["password"],
                username = credentials["reddit"]["username"],
                password = credentials["reddit"]["password"],
                user_agent = credentials["reddit"]["user_agent"]
            )
        return None
