import os

PATH = os.path.dirname(__file__)    #配置文件中的变量需大写，否则不能识别
SECRET_KEY = 'qwertyuiop[]asdfghjkl;/,.mnbvcxz'  #若果涉及到session、cookie等需要用到
BABEL_DEFAULT_LOCALE = 'zh_CN'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@localhost:3306/myblog' #链接数据库    
                          #"postgresql://postgres:@localhost/mahjong"
REDIS_URL = 'redis://@localhost:6379/0'  # redis
DEBUG = True
