import json
from listener import Listener
from constants import *
from application_context import ApplicationContext

def main():
    ac = ApplicationContext()  
    config = ac.getConfig()
    listener = FileListener(ac.performDownload, config.MessageQueueUrl(), config.MessageQueueUser(), config.MessageQueuePass() )
    listener.listen()

class FileListener(Listener):
    def __init__(self, performDownload, server, username, password):
        Listener.__init__(self, FILE_QUEUE_INBOUND,server, username, password)
        self._performDownload = performDownload

    def performAction(self, obj):
        self._performDownload(obj["url"])

if __name__ == "__main__":
    # execute only if run as a script
    main()