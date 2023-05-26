import os


class Config():
    ROOT = os.path.dirname(os.path.abspath(__file__))
    LOG_NAME = os.path.join(ROOT, 'logs', 'yala.log')
    JSON_AS_ASCII = False


    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PWD = 'FutS-Sbpu7fj'
    DBNAME = 'yala'



    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(MYSQL_USER,MYSQL_PWD,MYSQL_HOST,MYSQL_PORT,DBNAME)

    SQLALCHEMY_TRACK_MODIFICATIONS = False