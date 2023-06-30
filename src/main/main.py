import src.main.configurations as Configurations
import src.main.delegators.delegator as Delegator
import src.main.delegators.delegator_factory as DelegatorFactory
import src.main.delegators.delegator_types as DelegatorTypes
import src.main.delegators.reddit_delegator as RedditDelegator
import src.main.delegators.ssd_delegator as SsdDelegator

''' SCRATCH
posts_per_retrieval = 10
request_time_interval = 300.0
'''

def get_reddit_delegator(self, configs: dict) -> RedditDelegator:
    username = configs["username"]
    password = configs["password"]
    client_id = configs["client_id"] 
    client_pw = configs["client_pw"]
    user_agent = configs["user_agent"]
    return RedditDelegator(username, password, client_id, client_pw, user_agent)


def get_ssd_delegator(self, configs: dict) -> SsdDelegator:
    pass


def get_configs(filename: str) -> dict:
    return Configurations.get_credentials_from_json(filename)


def run_bot(reddit: RedditDelegator, ssd: SsdDelegator) -> None:
    pass


def get_delegators(config_uri):
    configs = get_configs(config_uri)
    reddit = get_reddit_delegator(configs["reddit"])
    ssd = get_ssd_delegator(configs["ssd"])
    return reddit, ssd
        

def run():
    reddit, ssd = get_delegators("../../configurations.json")
    run_bot(reddit, ssd)


if __name__ == '__main__':
    run()