import yaml

class Config(object):
    
    def MessageQueueUrl(self):
        raise NotImplementedError("Should be implemented")
    
    def MessageQueueUser(self):
        raise NotImplementedError("Should be implemented")
    
    def MessageQueuePass(self):
        raise NotImplementedError("Should be implemented")    
    
    def RedditUser(self):
        raise NotImplementedError("Should be implemented")    

    def RedditLimit(self):
        raise NotImplementedError("Should be implemented")    
    
    def RedditPass(self):
        raise NotImplementedError("Should be implemented")
    
    def DatabaseEngine(self):
        raise NotImplementedError("Should be implemented")
    
    def DatabaseLocation(self):
        raise NotImplementedError("Should be implemented")
    
    def FileStoreLocation(self):
        raise NotImplementedError("Should be implemented")
                