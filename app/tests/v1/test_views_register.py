import unittest
import json

from app.tests.v1.test_db import TestBase
from app import create_app, migration

class UserRegisterTestCase(TestBase):

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

        # self.assertIn('coolkid', str(response.data))
        self.assertEqual(response.status_code, 201)


    
    