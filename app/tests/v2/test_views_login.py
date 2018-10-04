"""Test for for testing the login endpoint"""
import unittest
import json

from app import create_app, migration

class UserLoginTestCase(unittest.TestCase):
    """Unit testiing for the user regsitration endpoint"""
    def setUp(self):
        """Initialize the app and database connections"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
    
        with self.app.app_context():
            migration.main(config='testing')

    def test_user_login(self):
        """Tests if the correct credentials were supplied"""
        response = self.client().post('/api/v2/auth/login', data=json.dumps({
            "username":"molly",
            "password":"1234",
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn("Successfully logged in", str(response.data))
    
    def test_user_empty_credentials(self):
        """Tests if no credentials were supplied"""
        response = self.client().post('/api/v2/auth/login', data=json.dumps({
            "username":"",
            "password":"",
        }), content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertIn("Error logging in, credentials not found", str(response.data))
    
    def test_user_no_credentials(self):
        """Tests if a user does not exist"""
        response = self.client().post('/api/v2/auth/login', data=json.dumps({
            "username":"kim",
            "password":"pass",
        }), content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertIn("Error logging in, credentials not found", str(response.data))
        