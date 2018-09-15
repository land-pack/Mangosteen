from app.core.log import logger


def bar_event(ch, method, properties, body):
    logger.warning(" [x] Received %s",body)
