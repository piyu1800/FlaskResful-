from enum import unique
import bcrypt as bcrypt
from test_app import db, app
from datetime import datetime

class User(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)


    def save(self):
        db.session.add(self)
        db.session.commit()   

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()