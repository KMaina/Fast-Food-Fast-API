import psycopg2
from flask import request, jsonify

from app import migration
from app.api.v2.model_users import get_user_id

connection = migration.db_connection()
cursor = connection.cursor()

class Orders():
    """Class to handle orders"""
    def get_user_order(self, username):
        """Get all orders for a particular user in the database"""
        userid = get_user_id(username)
        try:
            orders_table = "SELECT * FROM orders WHERE user_id = {}".format(userid) 
            cursor.execute(orders_table)
            connection.commit()
            rows = cursor.fetchall()
            print(rows)
            user_orders = []
            if rows is not None and len(rows) > 0:
                for row in rows:
                    order_dict = {
                        "status" : row[1],
                        "meal_name" : row[2],
                        "order_quantity" : row[3],
                        "order_cost" : row[4]
                    }
                    user_orders.append(order_dict)
                return {"orders":user_orders}, 200
            return {'msg': 'No records to fetch'}, 404
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            connection.close()
            return {'Error', error}, 400
