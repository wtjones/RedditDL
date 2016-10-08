from sqlalchemy import *
from sqlalchemy.orm import relation, sessionmaker
from data.models import Base

class Url(Base):
    __tablename__ = 'url'
    id = Column(Integer, primary_key=True)
    url = Column(String(length=700), unique=True)
    file_reference = Column(String(length=1000))

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "Url(%r,%r)" % (self.url, self.file_reference)
