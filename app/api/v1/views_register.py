from flask import Flask, request
from flask_restful import Resource

from app.api.v1.model import Users

class UserRegister(Resource):
    """This class is used to register a new user"""
    def post(self):
        return Users().register_user(
            request.json['username'],
            request.json['password'],
            request.json['confirm_password'],
            request.json['email'],
            request.json['address'],
            request.json['telephone'],
            request.json['admin']
        )
    
class UserLogin(Resource):
    """This class is used to login a user"""
    def post(self):
        return Users().login(
            request.json['username'],
            request.json['password']
        )