import psycopg2
from flask import request, jsonify

from app import migration

connection = migration.db_connection()
cursor = connection.cursor()

class Orders():
    """Class to handle orders"""
    def get_user_order(self):
        """Get all orders for a particular user in the database"""
        try:
            orders_table = "SELECT * FROM orders"
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
                        "order_cost" : row[4],
                        "user_id" : row[5]
                    }
                    user_orders.append(order_dict)
                return {"orders":user_orders}, 200
            return {'msg': 'No records to fetch'}, 404
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            connection.close()
        return {'Error', error}, 400