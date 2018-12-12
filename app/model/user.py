from app import db
from sqlalchemy.schema import Sequence
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import event
from sqlalchemy import DDL

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    pwd = db.Column(db.Unicode(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username
    
    @property
    def passwd(self):
        raise AttributeError('password is not a readable attribute!')
    
    @passwd.setter
    def passwd(self, passwd):
        self.pwd = generate_password_hash(passwd)
    
    def verify_password(self, passwd):
        return check_password_hash(self.pwd, passwd)

