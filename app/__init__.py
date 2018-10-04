"""
the __init__.py file

included to make app a package
"""

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from app.api.v2.views_users import UserRegister, UserLogin
from app.api.v2.views_menu import Menu

from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    api_endpoint = Api(app)
    api_endpoint.add_resource(UserRegister, '/api/v2/auth/signup')
    api_endpoint.add_resource(UserLogin, '/api/v2/auth/login')
    api_endpoint.add_resource(Menu, '/api/v2/menu')

    jwt = JWTManager(app)

    return app