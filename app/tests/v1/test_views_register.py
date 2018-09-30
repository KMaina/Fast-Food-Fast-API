import unittest
import json

from app import create_app, migration

class UserRegisterTestCase(unittest.TestCase):
    """Unit testiing for the user regsitration endpoint"""
    def setUp(self):
        """Initialize the app and database connections"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
    
        with self.app.app_context():
            migration.main(config='testing')

    def test_register_user(self):
        response = self.client().post('/api/v2/auth/signup', data = json.dumps({
            "username" : "coolkid",
            "password" : "123",
            "confirm_password" : "123",
            "email" : "coolkid@me.com",
            "address" : "Langata, Nairobi",
            "telephone" : "+712249175",
            "admin" : False
        }), content_type = 'application/json')

        self.assertEqual(response.status_code, 201)
