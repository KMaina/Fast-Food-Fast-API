"""The menu endpoints"""
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.v2.model_menu import Meals

class Menu(Resource):
    """This is the class to add and get meals in the menu"""   
    @jwt_required
    def get(self):
        """Method to get all meals"""
        return Meals().get_all_meals()
