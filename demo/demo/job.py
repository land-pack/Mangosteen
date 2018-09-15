from apscheduler.schedulers.background import BlockingScheduler
from app.jobs.foo import foo_fun
from app.core.log import logger

if __name__ == '__main__':
    logger.warning("Starting job ...")
    scheduler = BlockingScheduler(timezone='UTC')
    scheduler.configure()
    scheduler.add_job(foo_fun, 'interval', seconds=5)
    scheduler.start()

