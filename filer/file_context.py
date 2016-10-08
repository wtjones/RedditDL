import urllib, uuid

class FileContext(object):
    def __init__(self, rootpath):
        self._rootpath = rootpath
    
    def download(self, url):
        #TODO: try and error to error queue
        result = "%s%s.%s" % (self._rootpath,uuid.uuid1(),"html")
        urllib.urlretrieve(url, result)
        return result