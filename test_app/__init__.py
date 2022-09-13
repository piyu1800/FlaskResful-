from flask import Flask, make_response, json,  request, jsonify
from flask_restful import Api
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(db,app)


if app.config['DEBUG']:
    app.debug = True

import test_app.routes.routes

@app.before_first_request
def create_table():
    db.create_all()