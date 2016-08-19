#-*- coding:utf-8 -*-
import logging
import time
# 设置默认的level为DEBUG
# 设置log的格式
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
    filename="log.log",
    filemode='w'
                )
# 记录log
while True:
    logging.debug('debug: ...')
    logging.info('info: ...')
    logging.warn('warning: ...')
    logging.error('error: ...')
    logging.critical('critical: ...')
    time.sleep(3)
