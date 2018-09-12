"""The test_views.py file

Runs unit tests on the views.py routes

"""

from app import app

def test_one_order():
    """Returns a 200 status code if an order is fetched"""
    response = app.test_client().get('/api/v1/order/1')

    assert response.status_code == 200

def test_one_order_fails():
    """Returns a 404 status code if an order is not fetched or found"""
    response = app.test_client().get('/api/v1/order/')

    assert response.status_code == 404
    