#!/usr/bin/python
# -*- coding:utf-8 -*-
# __author__ = 'yfz'
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
SECRET_KEY = '12343623623462'

class QXToken(object):
    """
    生成/验证　用户token
    """
    def __init__(self, name):
        self.name = name

    def generate_auth_token(self, expiration=3600):
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'name': self.name})

    def verify_auth_token(self, token):
        s = Serializer(SECRET_KEY)
        try:
            print type(s), s
            data = s.loads(token)
        except SignatureExpired:
            return -2         # valid token, but expired
        except BadSignature:
            return -1         # invalid token
        return data['name'] == self.name


def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class MyClass1(object):
    aa = 56


instance1 = MyClass1()
instance2 = MyClass1()
print id(instance1)
print id(instance2)

qxtoken = QXToken(1111)
token = qxtoken.generate_auth_token()
# token = 'eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ3MDkxOTU0MCwiaWF0IjoxNDcwOTE1OTQwfQ.eyJuYW1lIjoxMTExfQ.60lJDekwEtWeBsEcfp9C6R7x_SjFJqCCQW4_4EPKBF0'
# print token
q = QXToken(1111)
res = q.verify_auth_token(token)
print type(res), res
# print q.verify_auth_token(token)

