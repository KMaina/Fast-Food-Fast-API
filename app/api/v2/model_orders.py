import psycopg2
from flask import request, jsonify

from app import migration
from app.api.v1.model import get_user_id

connection = migration.db_connection()
cursor = connection.cursor()

class Orders():
    """Class to handle orders"""
    def get_user_order(self, username):
        """Get all orders for a particular user in the database"""
        userid = get_user_id(username)

        try:
            orders_table = "INSERT INTO orders \
                            (status_id, user_id, total_cost) \
                            VALUES \
                            (1, '{}' , '{}') RETURNING order_id" .format(active_user , total_cost) 
            
            cursor.execute(orders_table)
            connection.commit()
            return {'msg':'Order successfully created'}, 201
        except (Exception, psycopg2.DatabaseError) as error:
            print('h')
            connection.close()
            return {'Error', error}, 400
