import hashlib
from datetime import timedelta,datetime

import jwt
from jwt.exceptions import ExpiredSignatureError

EXPIRED_HOUR = 3

class UserToken(object):
    key = 'yalaToken'
    salt = 'yala'

    @staticmethod
    def get_token(data):
        new_data = dict({'exp':datetime.utcnow()+timedelta(EXPIRED_HOUR)}, **data)
        '''utc时间 +3`'''
        return jwt.encode(new_data, key=UserToken.key)
        '''encode编码，字符串→二进制，decode相反'''


    @staticmethod
    def parse_token(token):
        try:
            return jwt.decode(token, key=UserToken.key)
        except ExpiredSignatureError:
            raise Exception('token已过期，请重新登录')

    @staticmethod
    def add_salt(password):
        m = hashlib.md5()
        bt = f'{password}{UserToken.salt}'.encode('utf-8')
        m.update(bt)
        return m.hexdigest()

