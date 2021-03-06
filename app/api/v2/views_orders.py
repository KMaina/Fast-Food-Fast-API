from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.v2.model_orders import Orders

class UserOrders(Resource):
    """Method to add and get orders"""
    @jwt_required
    def get(self):
        """Method to get all a user's orders"""
        current_user = get_jwt_identity()

        return Orders().get_user_order(current_user['username'])
      
    @jwt_required
    def post(self):
        """Method to add a food item"""
        current_user = get_jwt_identity()
        
        return Orders().add_order(
            current_user['username'],
            request.json['meal_item'],
            request.json['order_quantity'],
            request.json['order_cost']
        )
