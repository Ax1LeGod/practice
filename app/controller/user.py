from flask import request
from flask import Blueprint
from flask import jsonify
from handler.factory import ResponseFactory
from app.dao.auth.UserDao import UserDao, UserToken

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['POST'])
def register():

    data = request.get_json()
    username, password = data.get('username'), data.get('password')
    if not username or not password:
        return jsonify(dict(code=101, msg='用户名和密码不能为空'))
    email, name = data.get('email'), data.get('name')
    if not email or not name:
        return jsonify(dict(code=101, msg='姓名和邮箱不能为空'))
    err = UserDao.register_user(username, password, email, name)
    if err is not None:
        return jsonify(dict(code=110, msg=err))
    return jsonify(dict(code=200, msg = '注册成功'))



@auth.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return jsonify(dict(code=101, msg="用户名或密码不能为空"))
    user, err = UserDao.login(username, password)
    if err is not None:
        return jsonify(dict(code=110, msg=err))
    user = ResponseFactory.model_to_dict(user, "password")
    token = UserToken.get_token(user)
    if err is not None:
        return jsonify(dict(code=110, msg=err))
    return jsonify(dict(code=0, msg="登录成功", data=dict(token=token, user=user)))
