from email import parser
from typing_extensions import Required
from urllib import request
from flask_restful import Resource, reqparse
from test_app import app 
from flask import make_response
from test_app.services.user_service import UserService

class Users(Resource):
    def get(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        
        args = parser.parse_args()
        print(args)
        return  UserService().get_user(args['username'])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, help='Name can not be blank', required=True)
        parser.add_argument("phone", type=str, required=True)
        parser.add_argument("email", type=str, required=True)

        args = parser.parse_args()

        return UserService().create_user(args['username'], args['phone'], args['email'])
