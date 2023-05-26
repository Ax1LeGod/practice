from app import yala

from app.utils.logger import Log
from app import dao

from app.controller.user import auth

yala.register_blueprint(auth)


@yala.route('/')
def helloworld():
    log = Log('helloworld专用')
    log.info('somebody viewed ur website')
    return 'helloworld'

if __name__ == '__main__':
    yala.run('0.0.0.0', threaded = True, port='7777')
