import configurations as Configurations
from src.main.delegators import RedditDelegator, SsdDelegator
from src.main.models import RedditPost, SsdSpec
from src.main.processors import RedditProcessor, SsdProcessor
from typing import Tuple #used for for method annotations

''' SCRATCH
posts_per_retrieval = 10
request_time_interval = 300.0
'''

def get_uncommented_posts(delegator: RedditDelegator, processor: RedditProcessor) -> list[RedditPost]:
    posts = delegator.get_posts()
    return processor.filter_posts_by_user(posts)


def get_reddit_delegator(configs: dict) -> RedditDelegator:
    return RedditDelegator(**configs)


def get_reddit_processor():
    return RedditProcessor()


def get_ssd_delegator(configs: dict) -> SsdDelegator:
    return SsdDelegator()


def get_ssd_processor() -> SsdProcessor:
    return SsdProcessor()


def get_delegators_from_configs(configs: dict) -> Tuple[RedditDelegator, SsdDelegator]:
    reddit = get_reddit_delegator(configs["reddit"])
    ssd = get_ssd_delegator(configs["ssd"])
    return reddit, ssd


def get_configs(filename: str) -> dict:
    return Configurations.get_credentials_from_json(filename)


def run_bot(reddit: RedditDelegator, ssd: SsdDelegator) -> None:
    """
    Goals:
    - Get recent posts
    - filter the posts we have commented on
    - Extract info from title
    - Get info of device
    - Prepare comment
    - Make comment
    - Wait 5 minutes
    """
    reddit_processor = get_reddit_processor()
    ssd_processor = get_ssd_processor()

    posts = get_uncommented_posts()
    for post in posts:
        title = reddit_processor.get_title(post)
        ssd_spec = ssd_processor.extract_info_from_str(title)

    pass
        

def run():
    configs = get_configs("../../configurations.json")
    reddit, ssd = get_delegators_from_configs(configs)
    run_bot(reddit, ssd)


if __name__ == '__main__':
    run()