"""
The views.py file.

All routes in the app are located here
"""

from flask import jsonify

from app import app

orders = [
    {
        'name': 'Hamburger',
        'quantity' : 3,
        'description' : 'Tasty chicken burger perfect as a snack.',
        'id' : 1
    },
    {
        'name': 'French Fries',
        'quantity' : 2,
        'description' : 'Perfectly salted for you.',
        'id' : 2
    },
    {
        'name': 'Pizza',
        'quantity' : 5,
        'description' : 'Large pizza great for movie nights.',
        'id' : 3
    }
]

@app.route('/api/v1/order/<int:order_id>', methods=['GET'])
def one_order(order_id):
    """Returns a JSON object and a status code"""
    order = [order for order in orders if order['id'] == order_id]
    if order:
        return jsonify({'order': order[0]}), 200
    if not order:
        return jsonify(message='Error, order not found'), 404
