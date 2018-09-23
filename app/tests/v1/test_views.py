"""The test_views.py file

Runs unit tests on the views.py routes

"""

import unittest
import json
from app import create_app

class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app.config['TESTING'] = True
        self.client = self.app.test_client
        self.order = {
	        "name": "Pizza",
	        "quantity": 2,
	        "description": "Perfect as a snack.",
	        "status": 0
        }   
        self.changed_order = {
	        "name": "Pizza",
	        "quantity": 2,
	        "description": "Perfect as a snack.",
	        "status": 1
        }   
    
    def test_add_an_order(self):
        """Test for adding an order"""
        response = self.client().post('/api/v1/orders', data=json.dumps(self.order), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    

    def test_get_all_orders(self):
        """Test for fetching all orders"""
        response = self.client().get('/api/v1/orders')
        self.assertEqual(response.status_code, 200)
    
    def test_get_specific_order(self):
        """Test for fetching a specific order"""
        response = self.client().get('/api/v1/order/1')
        self.assertEqual(response.status_code, 200)
    
    def test_change_an_order_change(self):
        """Test for changing an order"""
        response = self.client().post('/api/v1/orders', data=json.dumps(self.order), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client().put('/api/v1/order/1', data=json.dumps(self.changed_order), content_type='application/json')
        result = self.client().get('/api/v1/order/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('1', str(result.data))   