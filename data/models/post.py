from data.models import Base
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
from sqlalchemy import UniqueConstraint
from subreddit import SubReddit
from url import Url


class Post(Base):
    __tablename__ = 'post'
    __table_args__ = (UniqueConstraint('user','url_id'),)
    id = Column(Integer, primary_key=True)
    user = Column(String(length=255))
    sub_reddit_id = Column(Integer, ForeignKey('subreddit.id'))
    title = Column(String(length=255))
    sub_reddit = relation("SubReddit", backref="subreddit", lazy=False)
    url_id = Column(Integer, ForeignKey('url.id'))
    url_instance = relation("Url", backref="url_instance", lazy=False)
    
    def __init__(self, user, title):
        self.user = user
        self.title = title

    def __repr__(self):
        return "Post(%r,%r)" % (self.title, self.user)
