class NotAuthenticatedError(Exception):
    def __init__(self):
        super().__init__("The user is not authenticated or logged into the correct account")

    def __str__(self):
        return self.message