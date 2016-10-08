from senders.sender import Sender
from constants import *

class RedditSender(Sender):
    
    def __init__(self,  server, username, password):    
            Sender.__init__(self, REDDIT_QUEUE_INBOUND, server, username, password)    