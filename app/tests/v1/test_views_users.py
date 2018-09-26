import unittest
import json
import os

from app import create_app
from flask_jwt_extended import JWTManager, create_access_token

class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        jwt = JWTManager(self.app)
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
        self.login = {
            'username' : 'kem1',
            'password' : '1234'
        }

    USERS_LIST = [
        {
	        'name' : "Ken Maina",
            'password' : "1234",
            'username' : "itsme",
            'email' : "ken@me.com",
            'address' : "Roysambu, Nairobi",
            'telephone' : "+712249175",
            'id' : 1,
            'admin' : True
        }
    ]
        
          
    
    def test_add_a_user(self):
        """Test for adding a user"""
        response = self.client().post('/api/v1/users', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_users(self):
        # response = self.client().get('/api/v1/users', content_type='application/json')
        # result = json.loads(response.data.decode())
        # print(result, file=sys.stderr)
        # self.assertEqual(result['name'], 'Ken Maina')
        pass

    def test_login_user(self):
        """Test for logging in a user"""
        response = self.client().post('/api/v1/users/login', data = json.dumps(self.login), content_type='application/json')
        # result = json.loads(response.data.decode())
        # self.assertEqual(response.status_code, 200)
        pass

    
    