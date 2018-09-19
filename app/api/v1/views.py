"""
The views.py file.

All routes in the app are located here
"""

from flask import request, json
from flask_restful import Resource

orders = []

class Orders(Resource):
    """
    GET/ all orders placed
    POST/ a new order
    """
    def get(self):
        """Return a list of all orders posted"""
        if len(orders) == 0:
            return {'messsage': 'Nothing found'}, 404
        return {'orders': orders}, 200

    def post(self):
        """Posts a specific order"""
        order_data = {}
        data = request.get_json()
        order_data['name'] = data['name']
        order_data['quantity'] = data['quantity']
        order_data['description'] = data['description']
        order_data['id'] = len(orders) + 1
        order_data['status'] = data['status']     
        orders.append(order_data)
        return {'orders': order_data}, 201

class OrderSpecific(Resource):
    """
    GET/ a specific order
    PUT/ edit a specific order
    DELETE/ delete a specific order 
    """
    def get(self, order_id):
        order = [order for order in orders if order['id'] == order_id]
        if order:
            return {'order': order[0]}, 200
        if not order:
            return {'message':'Error, order not found'}, 404
    
    def put(self, order_id):
        order = [order for order in orders if order['id'] == order_id]
        if order:
            data = request.get_json()
            order[0]['name'] = data['name']
            order[0]['quantity'] = data['quantity']
            order[0]['description'] = data['description']
            order[0]['status'] = data['status']     
            # orders.append(order_data)
            return {'order': order[0]}, 200
        if not order:
            return {'message':'Error, order not found'}, 404
    
    def delete(self, order_id):
        order = [order for order in orders if order['id'] == order_id]
        if order:
            del orders[0]
            return {'orders': orders}, 204
        else:
            return {'message': 'Could not find your order'}, 404
        
