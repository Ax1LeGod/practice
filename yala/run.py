from app import yala
from app.utils.logger import Log


@yala.route('/')
def helloworld():
    log = Log('helloworld专用')
    log.info('somebody viewed ur website')
    return 'helloworld'

if __name__ == '__main__':
    yala.run('0.0.0.0', threaded = True, port='7777')
