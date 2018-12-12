import os

PATH = os.path.dirname(__file__)    #配置文件中的变量需大写，否则不能识别
basedir = os.path.abspath(PATH)

class Config(): 
    SECRET_KEY = 'qwertyuiop[]asdfghjkl;/,.mnbvcxz'  #若果涉及到session、cookie等需要用到
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    REDIS_URL = 'redis://@localhost:6379/0'  # redis
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@localhost:3306/myblog' #链接数据库
    SQLALCHEMY_DATABASE_URI = 'postgresql://myblog:myblog@localhost/myblog'
                                        #[user][passwd]         [database]
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False  # 该配置为True,则每次请求结束都会自动commit数据库的变动
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪对象的修改并且发送信号，若为True(默认)则追踪会消耗额外的内存
   
    #oss
    ACCESS_KEY_ID = "********"
    ACCESS_KEY_SECRET = "***************"
    ALI_BUCKET = "**"
    ENDPOINT = "***"
    OSS_PHOTO_PREFIX = 'http://' + ALI_BUCKET + '.' + ENDPOINT + '/'
    DEFAULT_IMG = 'static/img/201809/20/153742_1bb3ed58.png'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    #email
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USER')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
#broker
    BROKER_URL = 'redis://localhost:6379/1'
    RESULT_BACKEND = 'redis://localhost:6379/2'
    DEFAULT_IMG = 'static/favicon.ico'


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    # 'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
