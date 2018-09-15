#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# Let's create a hello queue to which the message will be delivered
channel.queue_declare(queue='Something')
channel.basic_publish(
    exchange='',
    routing_key='Something',
    body='Hello World yyy Something')

print(' [x] Sent "Hello World!"')
channel.close()
