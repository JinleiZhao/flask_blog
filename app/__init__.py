#!/home/yaya/.pyenv/shims/python
#coding:utf-8

import redis
from flask import Flask
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell  
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import MetaData
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_moment import Moment  # 可以在浏览器中渲染日期和时间
from flask_mail import Mail
from config import config

app = Flask(__name__)

app.config.from_object(config['development']) #引入配置文件
# redis_store = FlaskRedis(app, strict=False) #redis
db = SQLAlchemy(app)

default_img = app.config['DEFAULT_IMG']
app.jinja_env.globals['DEFAULT_IMG'] = default_img

'''
#也可以db = SQLAlchemy()        db.init_app(app)
'''
admin = Admin(app) 

migrate = Migrate(app, db)   

manager = Manager(app)

manager.add_command('db', MigrateCommand)

# redis_client = redis.StrictRedis(host='locaohost',port=6379,db=0) #直接链接
redis_client = FlaskRedis(app) #通过配置文件链接

bootstrap = Bootstrap(app)

moment = Moment(app)

mail = Mail(app)
'''
@manager.command   #manage.py 跟上函数名则通过此函数启动
def fast_cgi():
    import os
    from flup.server.fcgi import WSGIServer    
    os.umask(0o600)
    WSGIServer(app, bindAddress='/tmp/vote.sock').run()
'''

'''添加的命令，没每次执行sheels时自动导入下面的参数'''


def make_shell_context():
    from .model.user import User, Role
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("sheels", Shell(make_context=make_shell_context))

@manager.option('-n','--name',dest='name',default='/tmp/myblog.sock') #将-n,--name 绑定到name这个变量上，默认为hello   
                                                          #python manage.py run_  [-n/--name]  [/home/xxx.sock 若不赋值则值是默认default] 执行命令
def run_(name):
    print('name',name)
    import os
    from flup.server.fcgi import WSGIServer
    os.umask(0o600)
    WSGIServer(app, bindAddress=name).run()

from app.route import views
from app.route import file_
from app.model.user import User
from app.route import home
from app.form import loginer