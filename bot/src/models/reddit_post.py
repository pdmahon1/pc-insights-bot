from praw.models import Submission

class RedditPost:
    def __init__(self, post:Submission):
        flair = post.link_flair_text
        title = post.title
        comments = post.comments #type: CommentForest