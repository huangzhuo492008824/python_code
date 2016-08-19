#!/usr/bin/python
#-*- coding:utf-8 -*-

import redis
from redis.exceptions import ConnectionError

class RedisQueue(object):  
    """Simple Queue with Redis Backend"""  
    def __init__(self, password, ip='localhost', port=6379):
        """The default connection parameters are: host=‘localhost‘, port=6379, db=0"""  
        self.password = password
        self.ip = ip
        self.port = port
        self._init_rd()

    def _init_rd(self):
        try:
            self.__db= redis.Redis(host=self.ip, port=self.port, db=0, password=self.password)
        except Exception as e:
            pass

    def qsize(self, key):
        try:
            return self.__db.llen(key)
        except ConnectionError as e:
            self._init_rd()
        
    def push(self, key, item):  
        """Put item into the queue."""
        try:
            self.__db.rpush(key, item)  
        except ConnectionError as e:
            self._init_rd()
  
    def pop(self, key, block=True, timeout=None):  
        """Remove and return an item from the queue.  
        If optional args block is true and timeout is None (the default), block 
        if necessary until an item is available."""  
        try:
            if block:  
                item = self.__db.blpop(key, timeout=timeout) 
                if item: 
                    return item[1]
            else:  
                item = self.__db.lpop(key) 
                return item
        except ConnectionError as e:
            self._init_rd()

    def set(self, key, item):
        try:
            self.__db.set(key, item)
        except ConnectionError as e:
            self._init_rd()

    def get(self, key):
        try:
            return self.__db.get(key)
        except ConnectionError as e:
            self._init_rd()

    def geoadd(self, collect, lng, lat, user_id):
        """
        :param collect: 集合名称
        :param lat:   纬度
        :param lng:   经度
        :param user_id: 用户id
        :return:
        """
        try:
            return self.__db.execute_command('geoadd', collect, lng, lat, user_id)
        except ConnectionError as e:
            self._init_rd()

    def georadiusbymember(self, collect, user_id, distance):
        """

        :param collect: 集合名称
        :param user_id: 用户id
        :param distance:距离单位：km
        :return:用户id列表
        """
        try:
            return self.__db.execute_command('georadiusbymember', collect, user_id, distance, 'km', 'withdist')
        except ConnectionError as e:
            self._init_rd()

    def geodist(self, collect, user_id, around_user_id):
        """
        计算两个用户之间的距离
        :param collect:
        :param user_id: 用户id
        :param around_user:  周围用户id
        :return: 用户之间距离（单位：km)
        """
        try:
            return self.__db.execute_command('geodist', collect, user_id, around_user_id, 'km')
        except ConnectionError as e:
            self._init_rd()

    def hmset(self, key, date=None, count=None, act_acount=None, distance=None):
        """
        设置用户当天发送弹幕条数
        :param key:
        :param date:
        :param count:
        :param act_count:
        :param distance:
        :return:
        """
        try:
            if distance:
                return self.__db.hmset(key, {'distance': distance})
            elif count:
                return self.__db.hmset(key, {'date': date, 'count': count})
            elif act_acount:
                return self.__db.hmset(key, {'date': date, 'act_count': act_acount})
        except ConnectionError as e:
            self._init_rd()

    def hmget(self, key, *args):
        """

        :param key:
        :param date:
        :param count:
        :return:
        """
        try:
            return self.__db.hmget(key, *args)
        except ConnectionError as e:
            self._init_rd()