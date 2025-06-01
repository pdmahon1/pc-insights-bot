'''
Interacts with the Reddit API using PRAW to request and retrieve data.
'''

import re 
import praw
from praw.models import Comment, ListingGenerator, Subreddit, Submission
from praw.models.reddit.subreddit import ContributorRelationship
from praw.reddit import Reddit

# from models.reddit_post import RedditPost

class RedditClient:
    
    _KNOWN_TAGS = ["cpu", "gpu", "ssd"]
    _BOT_NAME = ""

    # used for quickly referencing Submissions the bot has commented on
    _RECENT_SUBMISSIONS_COMMENTED_ON = []
    _RECENT_SUBMISSIONS_COMMENTED_ON_POINTER = 0
    _RECENT_SUBMISSIONS_MAX_SIZE = 20

    def __init__(self, site_name):
        _reddit = Reddit(site_name)
        _BOT_NAME = site_name


    # @staticmethod
    # def create_reddit_instance(praw_ini_section_name) -> None:
    #     if(praw_ini_section_name not in Reddit._INSTANCES):
    #         Reddit._INSTANCES[praw_ini_section_name] = praw.Reddit(praw_ini_section_name)
                 

    # @staticmethod
    # def get_reddit_instance(praw_ini_section_name:str) -> Reddit:
    #     print("in Reddit.get_reddit_instance(str) with section name:", praw_ini_section_name)
    #     reddit = praw.Reddit(praw_ini_section_name)
    #     print("reddit instance = ", reddit)
    #     return reddit


    def verify_authenticated(self):
        return not self._reddit.read_only


    def get_tag_from_submission(self, submission:Submission):
        # transforms ["cpu", "gpu", "ssd"] to "(cpu|gpu|ssd)"
        tags_group = "|".join(self._KNOWN_TAGS)        
        
        # example: return "ssd" from "[SSD] WD SN850X..."
        matches = re.findall(f"({tags_group})", submission.name, re.IGNORECASE)
        return matches[0] if len(matches) > 0 else None


    def is_tag_supported(self, tag:str) -> bool:
        return tag in self._KNOWN_TAGS


    def get_subreddit(self, subreddit_name:str) -> Subreddit:   
        return self._reddit.subreddit(subreddit_name)


    def get_newest_posts(self, subreddit_name, max_posts:int = 10) -> ListingGenerator:
        return self.get_subreddit(subreddit_name).new(limit = max_posts)


    def has_bot_commented(self, submission:Submission) -> bool:
        assert submission is not None, "has_bot_commented() - submission was None"
        # quickly references Submissions most recently commented on
        if submission.id in self._RECENT_SUBMISSIONS_COMMENTED_ON:
            return True
        
        for comment in submission.comments:
            if(comment.author.lower() == self._BOT_NAME):
                return True
            
        return False


    # @staticmethod
    # def get_recent_posts(self, subreddit:Subreddit) -> list:
    

    # @staticmethod
    # def sleep_time():
    #     return Reddit._INTERVAL_BETWEEN_REQUESTS


    def send_comment(comment:Comment, submission:Submission) -> bool:
        # use PRAW to send a comment to the specific submission
        pass

    def add_comment_to_recents(self, submission:Submission) -> None:
        recents = self._RECENT_SUBMISSIONS_COMMENTED_ON
        max_size = self._RECENT_SUBMISSIONS_MAX_SIZE

        if(len(recents) == max_size):
            pointer = self._RECENT_SUBMISSIONS_COMMENTED_ON_POINTER
            recents[pointer] = submission.id
            self._RECENT_SUBMISSIONS_COMMENTED_ON_POINTER = (pointer+1) % max_size

        else:
            recents.append(submission.id)
