from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.v2.model_orders import Orders

class GetAllOrders(Resource):
    """Method to add and get orders"""
    @jwt_required
    def get(self):
        """Method to get all a user's orders"""
        current_user = get_jwt_identity()
        if current_user['admin'] == True:
            return Orders().get_user_order()
        return {'msg', 'Sorry you do not have sufficient rights to access this page'}, 403