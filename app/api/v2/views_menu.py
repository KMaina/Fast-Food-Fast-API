"""The menu endpoints"""
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.v2.model_menu import Meals

class Menu(Resource):
    """This is the class to add and get meals in the menu"""
    @jwt_required
    def post(self):
        """Method to add a meal to the menu"""
        current_user = get_jwt_identity()
        
        if current_user['admin'] == True:
            return Meals().add_menu(
                request.json['meal_name'],
                request.json['quantity'],
                request.json['description'],
                request.json['cost']
            )

        if current_user['admin'] == False:
            return {'msg':'Sorry, you do not have the rights to access this page'}, 403   
