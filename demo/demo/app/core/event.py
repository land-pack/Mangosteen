import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))


class Event(object):
    callback = {}
    channel = connection.channel()

    @classmethod
    def subscribe(cls, queue):
        def _wrapper(f):
            cls.callback[queue] = f.func_name
            cls.new(f, queue)

            def __wrapper(*argv, **kwargs):
                return f
            return __wrapper
        return _wrapper

    @classmethod
    def new(cls, func, queue, no_ack=True):
        cls.channel.queue_declare(queue)
        cls.channel.basic_consume(func, queue=queue, no_ack=no_ack)

    @classmethod
    def listen(cls):
        cls.channel.start_consuming()


@Event.subscribe("xxxx")
def test_event_x(ch, method, properties, body):
    print(" [X] Received %s", body)


@Event.subscribe("yyyy")
def test_event_y(ch, method, properties, body):
    print(" [Y] Received %s", body)


if __name__ == '__main__':
    Event.listen()
