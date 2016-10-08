from senders.sender import Sender
from constants import *

class PostSender(Sender):
    
    def __init__(self,  server, username, password):    
            Sender.__init__(self, POST_QUEUE_INBOUND, server, username, password)    