from sqlalchemy import event
from models.post import Post
from models.subreddit import SubReddit
from models.url import Url

class PostContext(object):
    
    def __init__(self, engine, session, urlCreated):
        self.engine = engine
        self.session = session
        self._urlCreated = urlCreated
        self._actions = []
        event.listen(self.session, "after_commit", self._commit)
    
    def _commit(self, session):
        for action in self._actions:
            action()
        self._actions = []

    def getSubreddit(self, name):
        return self.session.query(SubReddit).filter(SubReddit.name == name).first()

    def createSubReddit(self, name):
        result = SubReddit(name)
        self.session.add(result)
        self.session.commit()
        #self._actions.append(lambda: self.notification.subRedditCreated(name))
        return result
            
    def createUrl(self, url):
        result = Url(url)
        self.session.add(result)
        self.session.commit()
        self._actions.append(lambda: self._urlCreated(url))
        return result
    
    def getUrl(self, url):
        return self.session.query(Url).filter(Url.url == url).first()

    def createPostLink(self,subRedditName, user, url, title):
        post = Post(user, title)
        urlInstance = self.getUrl(url)
        if(urlInstance == None):
            urlInstance = self.createUrl(url)
        post.url_instance = urlInstance
        sub_reddit = self.getSubreddit(subRedditName)
        if(sub_reddit == None):
            sub_reddit = self.createSubReddit(subRedditName)
        post.sub_reddit = sub_reddit
        self.session.add(post)
        #self._actions.append(lambda: self.notification.postCreated(subRedditName, title, user, url))
        

    def getPostList(self, subRedditName, user, url, title):
        return self.session.query(Post).filter(Post.user == user, Post.title == title, SubReddit.name == subRedditName, Url.url == url ).first()

    def addFileReference(self, url, fileReference):     
        newurl = self.session.query(Url).filter(Url.url == url).first()
        if(newurl):
            newurl.file_reference = fileReference
            self.session.add(newurl)
        else:
            #TODO: some error
            pass