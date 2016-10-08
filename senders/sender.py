import pika, json

class Sender(object):

    def __init__(self, queue, server, username, password):
        self._queue = queue
        self._server = server
        self._user = username
        self._pass = password
    
    def send(self,  data_to_send):
        data = json.dumps(data_to_send)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self._server, credentials=pika.PlainCredentials(self._user, self._pass, erase_on_connect=False)))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self._queue)
        print(" [x] Sent '%s!'" % (data))
        self.channel.basic_publish(exchange='',
                                   routing_key=self._queue,
                                   body=data)
        self.connection.close()
        

    