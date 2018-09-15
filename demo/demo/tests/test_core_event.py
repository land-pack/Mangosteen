#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# Let's create a hello queue to which the message will be delivered
channel.queue_declare(queue='yyyy')
channel.basic_publish(
    exchange='',
    routing_key='yyyy',
    body='Hello World yyy')

print(' [x] Sent "Hello World!"')
channel.close()
