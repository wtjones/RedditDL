from constants import *
import json
from sqlalchemy import *
from sqlalchemy.orm import relation, sessionmaker
from sqlite3 import dbapi2 as sqllite
from data.models import Base
from senders import FileSender
from senders import RedditSender
from senders import PostSender
import sys
from data.post_notification import PostNotification
from sqlalchemy.ext.declarative import declarative_base
from data.post_context import PostContext
from reddit import RedditContext
from config_processor import ConfigProvider
from filer import FileContext

class ApplicationContext(object):
    def __init__(self):
        self._config = ConfigProvider("config.yaml").resolve()
        self._engine = create_engine('%s:///%s' % (self._config.DatabaseEngine(), self._config.DatabaseLocation()))
        Base.metadata.create_all(self._engine)
        self._session = sessionmaker(bind=self._engine, autoflush=False)()
        self._postContext = PostContext(self._engine, self._session, self.enqueueFile)
        self._fileContext = FileContext(self._config.FileStoreLocation())     
        self._redditContext = RedditContext(self._config.RedditUser())     
        self._redditSender = RedditSender(self._config.MessageQueueUrl(), self._config.MessageQueueUser(), self._config.MessageQueuePass())        
        self._postSender =  PostSender(self._config.MessageQueueUrl(), self._config.MessageQueueUser(), self._config.MessageQueuePass())
        self._fileSender =  FileSender(self._config.MessageQueueUrl(), self._config.MessageQueueUser(), self._config.MessageQueuePass())
        
    def getConfig(self):
        return self._config
    
    def createFileReference(self, url, fileReference):
        self._postContext.addFileReference(url, fileReference)
        try:
            self._session.commit()
        except:
            print 'rollbacked %s' % (sys.exc_info()[0])
            self._session.rollback()               
        
    def performDownload(self, url):
        self._postSender.send({"action":"processFileReference",
                                 "url":url,
                                 "fileReference":self._fileContext.download(url)})
        
    def getPosts(self, subreddit, pullType, limit):
        limit = min(limit, self.getConfig().RedditLimit())
        
        for post in self._redditContext.getPosts(subreddit, pullType, limit):
            self.enqueuePost(subreddit, post["user"], post["url"], post["title"])
            
    def processPost(self, subreddit, user, url, title):
        self._postContext.createPostLink(subreddit, user, url, title)
        try:
            self._session.commit()
        except:
            print 'rollbacked %s' % (sys.exc_info()[0])
            self._session.rollback()       
            
    def enqueueGetPostsFromReddit(self, subreddit, pullType, limit):
        self._redditSender.send({"subreddit": subreddit, 
                                 "pullType": pullType, 
                                 "limit": limit})
    def enqueuePost(self, subreddit, user, url, title):
        self._postSender.send({"action":"processPost","subReddit":subreddit, "user":user, "url":url, "title":title})
    def enqueueFile(self, url):
        self._fileSender.send({"url":url})