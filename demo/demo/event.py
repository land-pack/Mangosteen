import pika
from app.events.bar import bar_event

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(bar_event,
                      queue='hello',
                      no_ack=True)


print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
