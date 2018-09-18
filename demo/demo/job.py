from app.core.log import logger
from app.core.job import Job
from app.jobs import *


if __name__ == '__main__':
    logger.warning("Starting job ...")
    Job.run()
