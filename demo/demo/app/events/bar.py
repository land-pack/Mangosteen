from app.core.log import logger
from app.core.event import Event


@Event.subscribe("Something")
def bar_event(ch, method, properties, body):
    logger.warning(" >>>>>] Received %s",body)

