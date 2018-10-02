"""The menu endpoints"""
from flask import request
from flask_restful import Resource

from app.api.v1.menu_model import Meals

class Menu(Resource):
    """This is the class to add and get meals in the menu"""
    def post(self):
        """Method to add a meal to the menu"""
        return Meals().add_menu(
            request.json['meal_menu'],
            request.json['quantity'],
            request.json['description'],
            request.json['cost']
        )