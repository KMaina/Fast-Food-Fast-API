"""This module is used to interact with the database to handle all menu resources"""
import psycopg2
from flask import request, jsonify

from app import migration

connection = migration.db_connection()
cursor = connection.cursor()

class Meals():
    """Class to handle the menu"""
    def get_all_meals(self):
        """Method to get all food items"""
        get_meals = "SELECT * FROM menus"
        cursor.execute(get_meals)
        rows = cursor.fetchall()
        meals_list = []
        if rows:
            for row in rows:
                meals_dict = {
                    "meal_name" : row[1],
                    "quantity" : row[2],
                    "description" : row[3],
                    "cost" : row[4]
                }
                meals_list.append(meals_dict)
            return {"meals" : meals_list}, 200
        else:
            return {"msg":"No meals found"}, 404