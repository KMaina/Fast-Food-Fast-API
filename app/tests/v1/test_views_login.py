import unittest
import json

class UserLoginTestCase(unittest.TestCase):
    """Unit testiing for the user regsitration endpoint"""
    def setUp(self):
        """Initialize the app and database connections"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
    
        with self.app.app_context():
            migration.main(config='testing')

    def test_register_user(self):
        response = self.client().post('/api/v2/auth/login', data = json.dumps({
            "username" : "coolkid",
            "password" : "123",
        }), content_type = 'application/json')

        self.assertEqual(response.status_code, 200)