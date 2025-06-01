#! ./venv-pc-insights-bot/bin/python3

from sys import exit, argv
from src.clients.reddit import *
from src.exceptions import not_authenticated_error as NotAuthenticatedError
from src.exceptions import configuration_error as ConfigurationError

# If PRAW is installed correctly and praw.ini is properly configured, the test will return 0.
# Otherwise, the script exits with a 1 to denote an issue exists.

_errors = 0

try:
    site = "pc-insights-bot" if len(argv) == 1 else argv[2]
    reddit = Reddit.get_reddit_instance(site)

    if Reddit.verify_authenticated(reddit):
        print("Test passes with valid 'pc-insights-bot' configuration in praw.ini")
    else:
        print("Could not verify authentication using praw.ini configuration")
        raise NotAuthenticatedError
except NotAuthenticatedError as e:
    print("ERROR: Exception thrown while testing the praw.ini configuration file.")
    print(e)
    _errors += 1

exit( 0 if (_errors == 0) else 1)