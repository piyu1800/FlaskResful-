from test_app import api 
from test_app.controller.hello_1 import HelloTest
from test_app.controller.user_controller import Users


api.add_resource(HelloTest, '/api/v1/hello')
api.add_resource(Users,'/api/v1/user')
