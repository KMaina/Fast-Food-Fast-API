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
    
    def test_add_a_user(self):
        """Test for adding a user"""
        pass
    

    def test_login_user(self):
        """Test for logging in a user"""
        pass
    
    def test_logout_user(self):
        """Test for fetching a specific order"""
        pass
    
    