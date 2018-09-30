import psycopg2
import os

from flask import request, jsonify
from app import migration

connection = migration.db_connection()
cursor = connection.cursor()

class Users():
    """Class to handle users"""
    
    def register_user(self, username, password, confirm_password, email, address, telephone, admin):
        
        if type(username) != str():
            response = jsonify({'msg' : 'Username must be a string'})
            response.status_code = 400
            return response
        
        if type(password) != str() and type(confirm_password) != str():
            response = jsonify({'msg' : 'Password must be a string'})
            response.status_code = 400
            return response
        
        if type(email) != str():
            response = jsonify({'msg' : 'Email must be a string'})
            response.status_code = 400
            return response
        
        if type(address) != str():
            response = jsonify({'msg' : 'Address must be a string'})
            response.status_code = 400
            return response
        
        if type(telephone) != str():
            response = jsonify({'msg' : 'UsTelephoneername must be a string'})
            response.status_code = 400
            return response
        
        if type(admin) != bool():
            response = jsonify({'msg' : 'Admin must be a boolean'})
            response.status_code = 400
            return response