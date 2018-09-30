import psycopg2
import os
# from passlib.hash import sha256_crypt

from flask import request, jsonify
from werkzeug.security import generate_password_hash
from app import migration

connection = migration.db_connection()
cursor = connection.cursor()

class Users():
    """Class to handle users"""
    
    def register_user(self, username, password, confirm_password, email, address, telephone, admin):
        
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        confirm_password = request.json.get('confirm_password', None)
        email = request.json.get('email', None)
        address = request.json.get('address', None)
        telephone = request.json.get('telephone', None)
        admin = request.json.get('admin', None)
        
        if type(username) != str:
            print(type(username))
            response = jsonify({'msg' : 'Username must be a string'})
            response.status_code = 400
            return response
        
        if type(password) != str and type(confirm_password) != str:
            response = jsonify({'msg' : 'Password must be a string'})
            response.status_code = 400
            return response
        
        if type(email) != str:
            response = jsonify({'msg' : 'Email must be a string'})
            response.status_code = 400
            return response
        
        if type(address) != str:
            response = jsonify({'msg' : 'Address must be a string'})
            response.status_code = 400
            return response
        
        if type(telephone) != str:
            response = jsonify({'msg' : 'UsTelephoneername must be a string'})
            response.status_code = 400
            return response
        
        if type(admin) != bool:
            response = jsonify({'msg' : 'Admin must be a boolean'})
            response.status_code = 400
            return response
        
        if password != confirm_password:
            response = jsonify({'msg' : 'Passwords must match'})
            response.status_code = 400
            return response
        
        try:
            hashed_password = generate_password_hash(password = password, method = 'pbkdf2:sha256', salt_length = 10)
            if admin == True:
                add_user = "INSERT INTO \
                            users \
                            (username, password, email, address, telephone, admin) \
                            VALUES \
                            ('" + username +"', '" + hashed_password +"', '" + email + "', '" + address + "', '" + telephone + "',  true )"
            if admin == False:
                add_user = "INSERT INTO \
                            users \
                            (username, password, email, address, telephone, admin) \
                            VALUES ('" + username +"', '" + hashed_password +"', '" + email + "', '" + address + "', '" + telephone + "',  false )"
            cursor.execute(add_user)
            
            cursor.close()
            connection.commit()
            response =  jsonify({'msg' : 'User successfully added to the databse'})
            response.status_code = 201
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error executing", error)
            response =  jsonify({'msg' : 'Problem inseting into the databse'})
            response.status_code = 400
            return response
        finally:
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")