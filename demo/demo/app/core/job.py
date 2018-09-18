from apscheduler.schedulers.background import BlockingScheduler


class Job(object):
    scheduler = BlockingScheduler(timezone='UTC')
    scheduler.configure()

    @classmethod
    def cron(cls, seconds=5):
        def _wrapper(f):
            cls.scheduler.add_job(f, 'interval', seconds=seconds)

            def __wrapper(*argv, **kwargs):
                return f
            return __wrapper
        return _wrapper

    @classmethod
    def run(cls):
        cls.scheduler.start()
