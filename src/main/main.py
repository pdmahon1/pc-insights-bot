import configurations as Configurations
import time
from praw.models import Subreddit
import src.main.clients
import src.main.factories
import src.main.models
import src.main.processors
import src.main.clients.reddit as Reddit

def run():
    try:
        configs = get_configs("../../configurations.json")
        Reddit.init(configs['reddit'])
        start_bot(configs)
    except FileNotFoundError:
        print("Could not find the configurations.json file")
        exit(1)
    exit(0)
    #X setup configs
    #start the bot
    #  get the next 10 posts
    #  for each post:
    #    skip this post if the bot already commented
    #    determine the item type
    #    for a supported type, extract data
    #    submit information on that item

def get_configs(filename:str) -> dict:
    return Configurations.get_credentials_from_json(filename)       

def start_bot(self, configs:dict):
    while True:
        for subreddit in configs["reddit"]["subreddits"]:
            handle_subreddit(subreddit)
        #sleep

def handle_subreddit(subreddit:str):
    posts = get_first_ten_posts(subreddit)
    for post in posts:
        if has_bot_commented_on_post(post):
            continue
        
if __name__ == '__main__':
    run()