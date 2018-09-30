"""
the __init__.py file

included to make app a package
"""

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from app.api.v1.views_register import UserRegister

from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    api_endpoint = Api(app)
    api_endpoint.add_resource(UserRegister, '/api/v2/auth/signup')

    jwt = JWTManager(app)

    return app