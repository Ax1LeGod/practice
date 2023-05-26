from sqlalchemy import or_
from datetime import datetime
from middleware.Jwt import UserToken
from app.models import db
from app.models.user import User
from app.utils.logger import Log


class UserDao(object):
    log = Log('UserDao')

    @staticmethod
    def register_user(username, password, email, name):

        try:
            users = User.query.filter(or_(User.username == username, User.email == email)).all()
            '''筛选用户名、邮箱是否已存在'''
            if users:
                raise Exception('用户名或邮箱已注册')
            pwd = UserToken.add_salt(password)
            user = User(username, name, pwd, email)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            UserDao.log.error(f'用户注册失败:{str(e)}')
            return str(e)
        return None

    @staticmethod
    def login(username, password):
        try:
            pwd = UserToken.add_salt(password)
            user = User.query.filter_by(username=username, password=pwd, deleted_at = None).first()
            '''匹配用户名、密码'''
            if user is None:
                return None, "用户名或密码错误"
            user.last_login_at = datetime.now()
            '''更新登录时间'''
            db.session.commit()
            return user, None
        except Exception as e:
            UserDao.log.error(f'用户{username}登录失败:{str(e)}')
            return None, str(e)