'''
reddit_processor.py

Processes the data retrieved from the Reddit API.
'''

from reddit_delegator import RedditDelegator 

class RedditProcessor:
    def __init__(self, subreddit_name):
        self.reddit = RedditDelegator(subreddit_name)
        self.subreddit = subreddit_name

    def get_new_posts(n):
        return reddit

def process_new_posts():
    new_posts = get_new_posts(10)
