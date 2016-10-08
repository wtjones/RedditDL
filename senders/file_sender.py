from senders.sender import Sender
from constants import *

class FileSender(Sender):
    
    def __init__(self,  server, username, password):    
            Sender.__init__(self, FILE_QUEUE_INBOUND, server, username, password)    