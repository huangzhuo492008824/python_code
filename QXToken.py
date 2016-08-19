#!/usr/bin/python
# -*- coding:utf-8 -*-
# __author__ = 'hz'
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

SECRET_KEY = '-2(xam5)mvnqucv_e-ij$40o0yk1c)-v2v@nb_#4=nzz=%7_&$'

class QXToken(object):
    """
    生成/验证　用户token
    """
    def __init__(self, name):
        self.name = name

    def generate_auth_token(self, expiration=3600):
        """
        生成token
        :param expiration:
        :return: 返回token字符串
        """
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'name': self.name})

    def verify_auth_token(self, token):
        """
        验证token
        :param token:
        :return:True:验证成功,-2：过期, -1:验证失败, False:验证失败
        """
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
            print 'data:', data
        except SignatureExpired:
            return -2         # valid token, but expired
        except BadSignature:
            return -1         # invalid token
        return data['name'] == self.name