import json
from listener import Listener
from constants import *
import sys
from application_context import ApplicationContext

def main():
    ac = ApplicationContext()
    config = ac.getConfig()
    listener = PostListener(ac.createFileReference, ac.processPost, config.MessageQueueUrl(), config.MessageQueueUser(), config.MessageQueuePass() )
    listener.listen()

class PostListener(Listener):
    def __init__(self, createFileReference, processPost, server, username, password):
        Listener.__init__(self, POST_QUEUE_INBOUND,server, username, password)
        self._createFileReference = createFileReference
        self._processPost = processPost

    def processPost(self, obj):
        self._processPost(obj["subReddit"], obj["user"], obj["url"], obj["title"])   
    def processFileReference(self, obj):
        self._createFileReference(obj["url"],obj["fileReference"])
    def performAction(self, obj):
        ({"processPost": self.processPost,
         "processFileReference": self.processFileReference}[obj["action"]])(obj)


if __name__ == "__main__":
    # execute only if run as a script
    main()