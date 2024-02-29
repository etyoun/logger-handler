import json
from logging import getLogger, config
from datetime import datetime


# 環境設定ファイル(JSON)を読み込む
with open("./setting/log_config.json", 'r') as f:
    log_conf = json.load(f)

# ファイル名をタイムスタンプで作成
log_conf["handlers"]["fileHandler"]["filename"] = \
    './data/logs/{}.logs'.format(datetime.now().strftime("%Y%m%d%H%M%S"))

# パラメータが設定されていればレベルをINFOからDEBUGに置換
# if ARGS.verbose:
#     log_conf["handlers"]["fileHandler"]["level"] = DEBUG

# logging設定
config.dictConfig(log_conf)

logger = getLogger(__name__)
logger.info('Process Start!')
logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.info('Process End!')
