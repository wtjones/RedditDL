import json, pika

class Listener(object):

    def __init__(self, queue, server, username, password):
        self.request_queue = queue
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(server,credentials=pika.PlainCredentials(username, password, erase_on_connect=False)))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.request_queue)

    def callback(self, ch, method, properties, body):
        self.performAction(json.loads(body))
    
    def performAction(self, obj):
        raise NotImplementedError("Implement should be implemented")
    
    def listen(self):
        self.channel.basic_consume(self.callback,
                              queue=self.request_queue,
                              no_ack=True)    
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
