"""
the __init__.py file

included to make app a package
"""

from flask import Flask
from flask_restful import Api

from app.api.v2.views_users import UserRegister, UserLogin

from instance.config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    api_endpoint = Api(app)
    api_endpoint.add_resource(Orders, '/api/v1/orders')
    api_endpoint.add_resource(OrderSpecific, '/api/v1/order/<int:order_id>')

    return app