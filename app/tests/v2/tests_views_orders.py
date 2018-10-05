"""Test for the add and get menu endpoint"""
import unittest
import json

from app import create_app, migration

class MenuTestCase(unittest.TestCase):
    """Unit testiing for the user regsitration endpoint"""
    def setUp(self):
        """Initialize the app and database connections"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
    
        with self.app.app_context():
            migration.main(config='testing')
            
        
    def test_get_orders(self):
        """Tests if a food item is added"""
        response = self.client().get('/api/v2/users/orders')
        self.assertAlmostEqual(response.status_code, 200)
    