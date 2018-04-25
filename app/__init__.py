#!/home/yaya/.pyenv/plugins/python
#coding:utf-8

import redis
from flask import Flask
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager  
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import MetaData

app = Flask(__name__)

app.config.from_object('config') #引入配置文件
# redis_store = FlaskRedis(app, strict=False) #redis
db = SQLAlchemy(app)

migrate = Migrate(app, db)   

manager = Manager(app)

manager.add_command('db', MigrateCommand)

# redis_client = redis.StrictRedis(host='locaohost',port=6379,db=0) #直接链接
redis_client = FlaskRedis(app) #通过配置文件链接

from app.route import views
from app.model.user import User
