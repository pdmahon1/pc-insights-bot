'''
reddit_delegator.py

Interacts with the Reddit API to request and retrieve data.
'''

import praw
from praw.models.reddit.subreddit import ContributorRelationship
from praw.reddit import Reddit

class RedditDelegator:

    def __init__(configs: map):
        if type(configs) is not map:
            output = "Credentials used to instantiate RedditDelegator should be a map.\n"
            output += "Type provided: {}".format(type(configs))
            raise TypeError(output)
        elif RedditDelegator.has_valid_credentials(configs) is False:
            raise ValueError("There are invalid credentials passed to RedditDelegator.")

        reddit = RedditDelegator.get_reddit_from_configs(configs)


    @staticmethod
    def has_valid_credentials(self, configs: dict) -> bool:
        """A simple credentials validator. 
        
        Checks for a username, password, and user-auth key in the credentials.
        If they exist and do not have empty values, then return true
        """
        REQUIRED_PROPS = ["username", "password", "client_id", "client_pw", "user-auth"]
        for prop in REQUIRED_PROPS:
            if prop not in configs:
                return False
            elif not (configs[prop] and type(configs[prop]) is "str"):
                return False
        return True
    
    @staticmethod
    def get_reddit_from_configs(configs:map) -> Reddit:
        return praw.Reddit(
            username = configs["username"],
            password = configs["password"],
            client_id = configs["client_id"],
            client_secret = configs["client_pw"],
            user_agent = configs["user_agent"]
        )


    def get_recent_posts(self, num_posts: int) -> list:
        return list()
