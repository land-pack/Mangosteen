import time
from app.core.log import logger
from app.core.event import Event


@Event.subscribe("Something")
def bar_event(ch, method, properties, body):
    logger.warning(" >>>>>] Received %s", body)

@Event.subscribe("new_queue")
def new_queue(ch, method, properties, body):
    for i in range(1000):
        time.sleep(1)
        logger.warning("Body --->%s -->%s", body, i)
