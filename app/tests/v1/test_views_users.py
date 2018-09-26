import unittest
import json
from app import create_app

class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app.config['TESTING'] = True
        self.client = self.app.test_client
        self.user = {
	        'name' : "Ken Maina",
            'password' : "1234",
            'username' : "itsme",
            'email' : "ken@me.com",
            'address' : "Roysambu, Nairobi",
            'telephone' : "+712249175",
            'id' : 1,
            'admin' : True
        }   
          
    
    def test_add_a_user(self):
        """Test for adding a user"""
        response = self.client().post('/api/v1/users', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        """Test for logging in a user"""
        response = self.client().post('/api/v1/users/login', data = json.dumps(self.user), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_logout_user(self):
        """Test for fetching a specific order"""
        pass
    
    