"""
the __init__.py file

included to make app a package
"""
import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from app.api.v1.views_orders import Orders, OrderSpecific

from app.api.v1.views_users import UserRegistration, UserLogin

from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.secret_key = os.getenv('SECRET_KEY')
    api_endpoint = Api(app)
    api_endpoint.add_resource(Orders, '/api/v1/orders')
    api_endpoint.add_resource(OrderSpecific, '/api/v1/order/<int:order_id>')
    api_endpoint.add_resource(UserRegistration, '/api/v1/users')
    api_endpoint.add_resource(UserLogin, '/api/v1/users/login')

    jwt = JWTManager(app)

    return app