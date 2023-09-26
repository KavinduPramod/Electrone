from __init__ import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    register_number = db.Column (db.String(100), )
    username = db.Column(db.String(100),unique=True)
    password = db.Column(db.Integer,unique=True)

class User_role(db.Model):
    __tablename__="user_role"
    id = db.Column(db.Integer, primary_key=True)
    user_role = db.Column (db.String(100))
