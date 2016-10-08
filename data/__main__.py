from sqlalchemy import *
from sqlalchemy.orm import relation, sessionmaker
from sqlite3 import dbapi2 as sqllite
from models import Base
import sys
from post_context import PostContext
from post_notification import PostNotification
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('sqlite+pysqlite:///reddit.db')
#Base.metadata.create_all(engine)
#session = sessionmaker(bind=engine, autoflush=False)()

#pc = PostContext(engine, session, PostNotification())

#pc.createPostLink("news","tester1","http://google.com","Search Engine")
#pc.createPostLink("news","tester2","http://google.com","Search Engine 123")
#pc.createPostLink("news","tester3","http://google.com","Search Engine 1235")
try:
    session.commit()
except:
    print 'rollbacked %s' % (sys.exc_info()[0])
    session.rollback()            

# Read by URL

# Update file reference
