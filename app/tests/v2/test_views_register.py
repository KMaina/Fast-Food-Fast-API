"""Test for for testing the register endpoint"""
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
        """Method to test if a user is successfully registered"""
        response = self.client().post('/api/v2/auth/signup', data=json.dumps({
            "username" : "molly",
            "password" : "123",
            "confirm_password" : "123",
            "email" : "molly@me.com",
            "address" : "Langata, Nairobi",
            "telephone" : "+712249175",
            "admin" : False
        }), content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertIn("User successfully added to the database", str(response.data))
    
    def test_register_wrong_parameters(self):
        """Method to test if a user is successfully registered"""
        response = self.client().post('/api/v2/auth/signup', data=json.dumps({
            "username" : "molly",
            "password" : 123,
            "confirm_password" : "123",
            "email" : "molly@me.com",
            "address" : "Langata, Nairobi",
            "telephone" : "+712249175",
            "admin" : False
        }), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertIn("Password must be a string", str(response.data))

