from flask_restful import Resource, reqparse
from flask import json, request, Flask
# from flask_jwt_extended import jwt_required
from app.api.v1.models import Users

class UserRegistration(Resource):

    def post(self):
        """Register a new user"""
        parser = reqparse.RequestParser()

        parser.add_argument('name', required=True, help='Name must be supplied')
        parser.add_argument('password', required=True, help='Password must be supplied')
        parser.add_argument('username', required=True, help='Username has to be supplied')
        parser.add_argument('email', required=True, help='Email has to be supplied')
        parser.add_argument('address', required=True, help='Address has to be supplied')
        parser.add_argument('telephone', required=True, help='Telephone number has to be supplied')
        parser.add_argument('admin', required=True, help='Admin status is to be supplied as a bool')

        # Parse the arguments into an object
        args = parser.parse_args()

        return Users().register_user(
            name = request.json['name'], 
            password =  request.json['password'], 
            username = request.json['username'],
            email =  request.json['email'],
            address =  request.json['address'],
            telephone =  request.json['telephone'],
            admin = request.json['admin']
        )
    
    def get(self):
        """Return all users"""
        return Users().get_all_users()

class UserLogin(Resource):

    def post(self):
        """Log in a users"""
        return Users().login_user(
            username = request.json['username'],
            password = request.json['password']
        )
    