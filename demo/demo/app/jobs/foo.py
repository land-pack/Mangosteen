from app.core.log import logger
from app.core.job import Job


@Job.cron(seconds=3)
def foo_fun():
    logger.warning("This is a test job")
