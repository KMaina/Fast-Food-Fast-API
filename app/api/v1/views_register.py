from flask import Flask, request
from flask_restful import Resource

class UserRegister(Resource):
    """This class is used to register a new user"""
    def post(self):
        pass