from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
from sqlalchemy import UniqueConstraint
from data.models import Base
class SubReddit(Base):
    __tablename__ = 'subreddit'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255), unique=True)
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "SubReddit(%r)" % (self.name)
