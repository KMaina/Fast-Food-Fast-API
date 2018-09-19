"""
the __init__.py file

included to make app a package
"""

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api_endpoint = Api(app)

from app.api.v1.views import Orders, OrderSpecific

api_endpoint.add_resource(Orders, '/api/v1/orders')
api_endpoint.add_resource(OrderSpecific, '/api/v1/order/<int:order_id>')
