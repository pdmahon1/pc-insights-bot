'''
reddit_processor.py

Processes the data retrieved from the Reddit API.
'''

import re
from src.main.factories.processor_factory import ProcessorFactory
from src.main.models.reddit_post import RedditPost


class RedditProcessor(object):
    '''
    A singleton class that handles the data returned from and sent to the Reddit API. 
    This class does not handle the API calls.
    '''
    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls = super(RedditProcessor, cls).__new__(cls)
        return cls._instance


    @staticmethod
    def is_post_usable(self, post:RedditPost) -> bool:
        if post.flair == "Expired":
            return False
        
        type = self.get_item_type_from_title(post.title)
        return ProcessorFactory.can_process(type)


    @staticmethod
    def get_item_type_from_title(title:str) -> str:
        '''
        Returns the type of item from the title as a string. 
        
        The typical post looks like:
            "[TYPE] <Brand> <Model> <META INFO> $PRICE"

        Returns an empty string if the TYPE doesn't exist at the start of the title
        '''
        match = re.match("^\[([\w. ]+)\]", title)
        
        #if title starts with [Mic], then group(0) == '[Mic]', group(1) == 'Mic'
        item_type = ""
        try:
            return match.group(1)
        except IndexError:
            return ""