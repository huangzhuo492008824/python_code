#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import ConfigParser
import logging
import logging.config
import logging.handlers
import multiprocessing
import singleton

#@singleton
class config():
    def __init__(self):
        config_path = os.path.abspath(os.path.dirname(__file__))
        print '__file__:', __file__ #current file name
        print 'current dir:', os.path.abspath(os.path.dirname(__file__))  # return current abs dir
        config_file = os.path.join(config_path, 'config.conf')
        print 'config_file:', config_file
        self.body = ConfigParser.ConfigParser()
        self.body.read(config_file)

    def get(self,block,key):
        return self.body.get(block,key)

#@singleton
class logger():
    def __init__(self):
        process_name = multiprocessing.current_process().name
        print 'process_name:', process_name
        cf = config()
        level_config = cf.get('log', 'level')
        file_path = cf.get('log', 'file_path')
        file_name = '%s-log.log' % process_name
        log_file = os.path.join(file_path, file_name)
        level = level_config.upper()
        level_dict = {'DEBUG': logging.DEBUG,
                      'INFO': logging.INFO,
                      'WARNING': logging.WARNING,
                      'ERROR': logging.ERROR,
                      'CRITICAL': logging.CRITICAL,
                      'NOTSET': logging.NOTSET
                     }
        log_level = level_dict.get(level, '')
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level)
        handler = logging.handlers.TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=10)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

cf = config()
print type(cf.get('geo', 'distance'))
# log = logger()

