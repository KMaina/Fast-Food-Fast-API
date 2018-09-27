import unittest
from app import create_app, connection_to_test

class TestBase(unittest.TestCase):
    """This is the base from which other tests will inherit"""

    def setUp(self):
        """Initialize the app and database connections"""
        self.app = create_app(configg_name="testing")
        self.client = self.app.test_client
    
        with self.app.app_context():
            connection_to_test()

    def tearDown(self):
        """tears down all the initializations"""
        with self.app.app_context():
            #pass