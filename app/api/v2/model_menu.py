"""This module is used to interact with the database to handle all menu resources"""
import psycopg2
from flask import request, jsonify

from app import migration

connection = migration.db_connection()
cursor = connection.cursor()

class Meals():
    """Class to handle the menu"""
<<<<<<< HEAD
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
=======
    def add_menu(self, meal_name, quantity, description, cost):
        """Method to add a meal to the database"""
        meal_name = request.json.get('meal_name', None)
        quantity = request.json.get('quantity', None)
        description = request.json.get('description', None)
        cost = request.json.get('cost', None)

        if not isinstance(meal_name, str):
            response = jsonify({'msg':'Meal_name must be a string'})
            response.status_code = 400
            return response

        if not isinstance(quantity, int):
            response = jsonify({'msg':'Quantity must be an int'})
            response.status_code = 400
            return response

        if not isinstance(description, str):
            response = jsonify({'msg':'Description must be a string'})
            response.status_code = 400
            return response
            
        if not isinstance(cost, int):
            response = jsonify({'msg':'Cost must be a string'})
            response.status_code = 400
            return response
        try:
            cursor.execute("INSERT INTO menus (meal_name, quantity, description, cost) VALUES (%s,%s,%s,%s);", (meal_name, quantity, description, cost))
            connection.commit()
            response = jsonify({"msg":"Meal successfully added to the database"})
            response.status_code = 200
            return response
        except (Exception, psycopg2.DatabaseError) as error:
                response = jsonify({'msg':error})
                response.status_code = 400
                return response
    
>>>>>>> develop
