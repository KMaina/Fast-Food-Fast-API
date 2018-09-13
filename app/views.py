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
        'id' : 1,
        'status': 0
    },
    {
        'name': 'French Fries',
        'quantity' : 2,
        'description' : 'Perfectly salted for you.',
        'id' : 2,
        'status': 0
    },
    {
        'name': 'Pizza',
        'quantity' : 5,
        'description' : 'Large pizza great for movie nights.',
        'id' : 3,
        'status': 0
    }
]

@app.route('/api/v1/orders', methods=['GET'])
def all_orders():
    """Return a JSON object of all orders made with a status code of 200"""
    return jsonify({'orders': orders}), 200
