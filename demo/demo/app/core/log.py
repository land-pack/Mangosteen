import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from logging.config import fileConfig

import app.core.color

prefix_path = os.path.dirname(os.path.abspath(__file__))
log_conf_path = os.path.join(prefix_path, '../../config/default_log.ini')
if not os.path.exists(log_conf_path):
    raise Exception("Cannot load log config's file")



process_name = sys.argv[0].split('.')[0]

if 'job' in process_name:
    log_conf_path = os.path.join(prefix_path, '../../config/job_log.ini')
elif 'event' in process_name:
    log_conf_path = os.path.join(prefix_path, '../../config/event_log.ini')
else:
    # stay with default
    pass
    
fileConfig(log_conf_path)
logger = logging.getLogger('root')


logger.warning("Logger starts with [%s], proceess argv [%s]", log_conf_path, sys.argv)

