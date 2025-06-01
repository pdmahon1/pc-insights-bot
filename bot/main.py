from configurations import Configurations
from src.clients.reddit import RedditClient
from src.exceptions.configuration_error import ConfigurationError
from src.exceptions.not_authenticated_error import NotAuthenticatedError

from praw.exceptions import RedditAPIException
from praw.models import Subreddit, Submission
from praw.reddit import Reddit

def run():
    try:
        configs = Configurations.get_configs_from_json_file("./bot/configurations.json")
        run_bot(configs)
    except FileNotFoundError:
        print("Could not find the configurations.json file")
        exit(1)
    except (NotAuthenticatedError, ConfigurationError, AssertionError) as e:
        print(e)
        exit(1)


    # except Exception as e:
    #     print("generic exception caught:\n", e)

    #X setup configs
    #start the bot



def run_bot(configs:dict):
    reddit = RedditClient("pc-insights-bot")
    assert reddit is not None, 'Could not create a Reddit client.'
    assert RedditClient.verify_authenticated(reddit), 'Failed authentication with Reddit API'
    # FUTURE USE: assert configs["clients"]["reddit"]["subreddits"], \
    #     'configs["clients"]["reddit"]["subreddits"] failed assertion'
    
    for submission in reddit.get_newest_posts("buildapcsales"):
        # skip posts we've already commented on
        if reddit.has_bot_commented(submission):
            continue
        
        # skip tags we don't know
        tag = reddit.get_tag_from_submission(submission)
        if not reddit.is_tag_supported(tag):
            print(f"'{tag}' is not a supported tag. Skipping submission #{submission.id}.")
            continue    

        # build the comment
        # submit the comment
        continue

    # after the loop, sleep?


# TODO when the bot runs on multiple subreddits
# def get_subreddits_from_configs(reddit:Reddit, configs:dict) -> list:
#     pass


if __name__ == '__main__':
    run()