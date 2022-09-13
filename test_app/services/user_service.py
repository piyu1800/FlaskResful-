from datetime import datetime, date, timedelta
import random
from test_app import app, db
from test_app.models.user_model import User
from flask import g, request
from flask import make_response
from sqlalchemy import false
class UserService:
    def create_user(self, username, phone, email):
        user = User.find_by_email(email)
        print("user......",user)
        if not user:
            user = User(username=username, email=email, phone=phone)
            print(user)
            user.save()
            print("user_save....", user.email)
            return make_response({"message":"user created successfully..."})
    
    def get_user(self, username):
        user = User.find_by_username(username)
        if user:
            return make_response({"user": user.email})