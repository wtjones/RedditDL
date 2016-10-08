import json
from listener import Listener
from constants import *
from application_context import ApplicationContext
from reddit import RedditContext

def main():
    ac = ApplicationContext()
    config = ac.getConfig()
    listener = RedditListener(ac.getPosts, config.MessageQueueUrl(), config.MessageQueueUser(), config.MessageQueuePass() )
    listener.listen()

class RedditListener(Listener):
    def __init__(self, getPosts, server, username, password):
        self._getPosts = getPosts
        Listener.__init__(self, REDDIT_QUEUE_INBOUND,server, username, password)

    def performAction(self, obj):
        self._getPosts(obj["subreddit"], obj["pullType"], int(obj["limit"]))
        
if __name__ == "__main__":
    # execute only if run as a script
    main()