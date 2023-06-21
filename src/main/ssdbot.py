import praw
import src.main.credentials as Credentials
import src.reddit.reddit_delegator as RedditDelegator

''' SCRATCH
posts_per_retrieval = 10
request_time_interval = 300.0
'''

def setup_spreadsheet():
    pass


def validate_credentials(credentials: map):
    if credentials.is_valid() is False:
        pass  # TODO need to validate


def get_reddit(credentials: map) -> Reddit:
    return RedditDelegator.get_reddit_object(credentials)


def get_credentials(filename):
    return Credentials.get_credentials_from_json(filename)

def run_bot(subreddits: list, reddit: Reddit):
    while True:
        reddit.get_recent_posts(10)


def get_bot_steup():
    credentials = get_credentials('../../credentials.json')
    reddit = get_reddit(credentials)
    return credentials, reddit


@staticmethod
def run():
    subreddits = ['BuildAPCSales', 'BAPCSalesCanada']
    credentials, reddit = get_bot_steup()
    run_bot(subreddits, reddit)


if __name__ == '__main__':
    run()