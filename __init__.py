from constants import *

from reddit import RedditContext
from config_processor import ConfigProvider
from filer import FileContext
from listener import Listener
from reddit_listener import RedditListener
from post_listener import PostListener
from file_listener import FileListener
from senders import RedditSender
from senders import PostSender


#config = ConfigProvider("config.yaml").resolve()
#print  (config.MessageQueueUrl(), config.MessageQueueUser(), config.MessageQueuePass() )


#sender = RedditSender(config.MessageQueueUrl(), config.MessageQueueUser(), config.MessageQueuePass())
#sender.send(["tester"])

#listener = RedditListener(config.MessageQueueUrl(), config.MessageQueueUser(), config.MessageQueuePass() )
#listener.listen()




#post_sender = PostSender(config.MessageQueueUrl(), config.MessageQueueUser(), config.MessageQueuePass())
#post_sender.send({"user":"tester","url":"http://www.burksbrand.com/12223","subReddit":"news","title":"new article 1"})

#post_listener = PostListener(pc, config.MessageQueueUrl(), config.MessageQueueUser(), config.MessageQueuePass())
#post_listener.listen()

#fc = FileContext(config.FileStoreLocation())
#file_listener = FileListener(fc, config.MessageQueueUrl(),  config.MessageQueueUser(), config.MessageQueuePass())