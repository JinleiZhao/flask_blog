from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Integer, nullable=False, default=0) 
    phone = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(255),nullable=False)