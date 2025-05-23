'''
Interacts with the Reddit API using PRAW to request and retrieve data.
'''

import praw
from praw.models import Subreddit
from praw.models.reddit.subreddit import ContributorRelationship
from praw.reddit import Reddit

from src.main.models.reddit_post import RedditPost

class Reddit:

    def __init__(self, **configs):
        reddit = praw.Reddit(
            client_id = configs["client_id"],
            client_secret = configs["client_secret"],
            username = configs["username"],
            password = configs["user_password"],
            user_agent = configs["user_agent"],
        )
        _POSTS_PER_RETRIEVAL = 10
        _INTERVAL_BETWEEN_REQUESTS = 300.0 #5 minutes


    @staticmethod
    def get_subreddit(self, subreddit_name:str) -> Reddit:
        return self.reddit.subreddit(subreddit_name)


    @staticmethod
    def get_recent_posts(self, subreddit:Subreddit) -> list:
        posts = subreddit.new(limit = self._POSTS_PER_RETRIEVAL)
        return [RedditPost(post) for post in posts]
    

    @staticmethod
    def sleep_time(self):
        return self._INTERVAL_BETWEEN_REQUESTS


    @staticmethod
    def verify_authenticated():
        print(reddit.user.me())

    def send_comment(comment) -> None:
        # use PRAW to send a comment to the specific post
        pass



    praw.Reddit("PC-Insights-Bot",
            "vmeGen@KxXHKB3",
            "_gP19kMmzfB9n-A0xZnpsw",
            "3iv7cSGdWViaFQlfgfK1ORYJa6ARIA",
            "Linux:PC-Insights-Bot:v0.0.1 (by /u/pdmahon1)")
    

reddit = praw.Reddit(
    client_id="_gP19kMmzfB9n-A0xZnpsw",
    client_secret="3iv7cSGdWViaFQlfgfK1ORYJa6ARIA",
    user_agent="Linux:PC-Insights-Bot:v0.0.1 (by /u/pdmahon1)",
    password="vmeGen@KxXHKB3",
    username="PC-Insights-Bot"
)
