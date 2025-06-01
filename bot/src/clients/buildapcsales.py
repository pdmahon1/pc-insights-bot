import reddit as RedditClient

class BuildAPCSales(RedditClient):
    _instance = None

    # Create as a singleton
    def __new__(self, cls):
        if cls._instance == None:
            cls._instance = super(BuildAPCSales, cls).__new__(cls)
        return cls._instance
    
    def __init__():
        pass


