"""
Initializes the flask app and mackes it a package
"""
import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from app.api.v2.views_users import UserRegister, UserLogin

from instance.config import app_config

def create_app(config_name):
    """Application Factory for the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.secret_key = os.getenv('SECRET_KEY')

    #Initialize and use Flask-RESTful
    api_endpoint = Api(app)
    api_endpoint.add_resource(UserRegister, '/api/v2/auth/signup')
    api_endpoint.add_resource(UserLogin, '/api/v2/auth/login')

    #Initialize and use Flask-JWT-Extended
    jwt = JWTManager(app)

    return app
