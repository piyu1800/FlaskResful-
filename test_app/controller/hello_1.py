from email import parser
from typing_extensions import Required
from urllib import request
from flask_restful import Resource, reqparse
from test_app import app 
from flask import make_response
from test_app.models.user_model import User

class HelloTest(Resource):
    def get(self):
        return "Hello Welcome to User Info Page"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=str, required=True)
        parser.add_argument("username", type=str, help='Name can not be blank', required=True)
        parser.add_argument("phone", type=str, required=True)
        parser.add_argument("email", type=str, required=True)

        args = parser.parse_args()
        return make_response(args)
