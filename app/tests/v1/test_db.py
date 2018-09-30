import unittest

from app import create_app, migration

class TestBase(unittest.TestCase):
    """This is the base from which other tests will inherit"""

    def setUp(self):
        """Initialize the app and database connections"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
    
        with self.app.app_context():
            # db_test_init.DatabaseTest().drop_tables()
            migration.main(config='testing')


    def tearDown(self):
        """tears down all the initializations"""
        with self.app.app_context():
            pass