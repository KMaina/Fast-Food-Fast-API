"""Test for the add and get menu endpoint"""
import unittest
import json

from app import create_app, migration

class MenuTestCase(unittest.TestCase):
    """Unit testiing for the user regsitration endpoint"""
    def setUp(self):
        """Initialize the app and database connections"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
    
        with self.app.app_context():
            migration.main(config='testing')

    def test_add_food_item(self):
        """Tests if a food item is added"""
        response = self.client().post('/api/v2/menu', data=json.dumps({
            "meal_name":"Pizza",
            "quantity":100,
            "description":"Snack",
            "cost":600
        }), content_type='application/json')
        self.assertAlmostEqual(response.status_code, 200)
        self.assertIn("Meal successfully added to the database", str(response.data))

    def test_add_food_wrong_parameters(self):
        """Tests if swrong parameter is supplied"""
        response = self.client().post('/api/v2/menu', data=json.dumps({
            "meal_name":"Pizza",
            "quantity":"100",
            "description":"Snack",
            "cost":600
        }), content_type='application/json')
        self.assertAlmostEqual(response.status_code, 400)
        self.assertIn("Quantity should be an int", str(response.data))
    
    def test_add_food_empty_parameters(self):
        """Tests if swrong parameter is supplied"""
        response = self.client().post('/api/v2/menu', data=json.dumps({
            "meal_name":"Pizza",
            "quantity":"",
            "description":"Snack",
            "cost":600
        }), content_type='application/json')
        self.assertAlmostEqual(response.status_code, 400)
        self.assertIn("Missing input", str(response.data))

    def test_get_food_item(self):
            """Tests if a food item is added"""
            response = self.client().get('/api/v2/menu')
            self.assertEqual(response.status_code, 200)