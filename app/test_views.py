"""The test_views.py file

Runs unit tests on the views.py routes

"""

from app import app

def test_all_orders():
    """Returns a status code of 200
    Tests if the route gets a list of all orders
    """
    response = app.test_client().get('/api/v1/orders')
    assert response.status_code == 200

def test_edit_order_fails():
    """Returns a 404 status code if the order is not found"""
    response = app.test_client().put('/api/v1/order/', data={'status': 1}, content_type='application/json')
    assert response.status_code == 404
