import os

PATH = os.path.dirname(__file__)    #配置文件中的变量需大写，否则不能识别
SECRET_KEY = 'qwertyuiop[]asdfghjkl;/,.mnbvcxz'  #若果涉及到session、cookie等需要用到
BABEL_DEFAULT_LOCALE = 'zh_CN'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@localhost:3306/myblog' #链接数据库
SQLALCHEMY_DATABASE_URI = 'postgresql://myblog:myblog@localhost/myblog'
                                       #[user][passwd]         [database]
SQLALCHEMY_COMMIT_ON_TEARDOWN = False  # 该配置为True,则每次请求结束都会自动commit数据库的变动
REDIS_URL = 'redis://@localhost:6379/0'  # redis
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪对象的修改并且发送信号，若为True(默认)则追踪会消耗额外的内存
ACCESS_KEY_ID = "********"
ACCESS_KEY_SECRET = "***************"
ALI_BUCKET = "**"
ENDPOINT = "***"
OSS_PHOTO_PREFIX = 'http://' + ALI_BUCKET + '.' + ENDPOINT + '/'
