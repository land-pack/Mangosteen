from app.core.event import Event
from app.core.log import logger
from app.events import *

if __name__ == '__main__':
    logger.warning(" [*] Waiting for messages. To exit press CTRL+C")
    Event.listen()
