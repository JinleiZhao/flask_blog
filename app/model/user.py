from app import db
from sqlalchemy.schema import Sequence
from sqlalchemy import event
from sqlalchemy import DDL

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer,primary_key=True) # db.Sequence('user_id_seq',start=1000),
    name = db.Column(db.String(255), nullable=False)  # ,unique=True 则此列 不能重复，否则抛错
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Integer, nullable=False, default=0) 
    phone = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(255),nullable=False)

    @property
    def set_id(self):
        return self.id+1000
