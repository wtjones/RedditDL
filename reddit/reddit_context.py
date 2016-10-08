import praw, json


class RedditContext(object):
    
    def __init__(self, user):        
        self._user = user
        version = "0.0.0.0.1"
        self.user_agent = "%s by /u/%s" % (version,user)
        self.r =praw.Reddit(user_agent=self.user_agent)

    def getPosts(self, subreddit, pullType, limit):
        return [{"title":submission.title,
         "user": submission.author.name,
         "url": submission.url} for submission in getattr(self.r.get_subreddit(subreddit),pullType)(limit=limit) if not submission.is_self]
        
#rc = RedditContext("479c1db3-9fa2-4637-abdd-447a53ffa9e4")
#print json.dumps(rc.getPosts("news", "get_new", 10))