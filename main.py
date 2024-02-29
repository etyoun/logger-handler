import json
from logging import getLogger, config


with open("./log_config.json", 'r') as f:
    log_conf = json.load(f)

config.dictConfig(log_conf)

logger = getLogger(__name__)
logger.info('Process Start!')
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.info('Process End!')
