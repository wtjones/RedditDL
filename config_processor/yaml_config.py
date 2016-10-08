import yaml
from config_processor import Config

class YamlConfig(Config):
    
    def __init__(self, path):
        with open(path, 'r') as myfile:
            yml = myfile.read()
            config = yaml.load(yml)
            self._request_queue = 'redditrequests'
            self._messagequeueServer = config["messagequeue"]["server"]
            self._messagequeueUser = config["messagequeue"]["user"]
            self._messagequeuePass = config["messagequeue"]["pass"]
            self._databaseEngine = config["database"]["engine"]
            self._databasePath = config["database"]["location"]
            self._fileStore = config["fileStore"]["location"]
            self._redditLimit = config["reddit"]["limit"]            
            self._redditUser = config["reddit"]["user"]
            self._redditPass = config["reddit"]["pass"]

    def MessageQueueUrl(self):
        return self._messagequeueServer
    
    def MessageQueueUser(self):
        return self._messagequeueUser
    
    def MessageQueuePass(self):
        return self._messagequeuePass
    
    def RedditUser(self):
        return self._redditUser
    
    def RedditPass(self):
        return self._redditPass

    def RedditLimit(self):
        return self._redditLimit
    
    def DatabaseEngine(self):
        return self._databaseEngine
    
    def DatabaseLocation(self):
        return self._databasePath
    
    def FileStoreLocation(self):
        return self._fileStore
    