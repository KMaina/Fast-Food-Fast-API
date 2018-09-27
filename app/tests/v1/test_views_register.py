import unittest
import json

from app.api.v1 import test_db

class UserRegisterTestCase(TestBase):

    def test_register_user(self):
        response = self.client().post('/api/v2/auth/signup', data = json.dumps(), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)