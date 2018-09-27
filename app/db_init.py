import os
import psycopg2
from psycopg2 import Error

def connection_to_main():
    """Function to connect to the main DB"""

    user = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    print(user, password, host, port, db_name)
    try:
        connection = psycopg2.connect(
                                      host=host,
                                      database=db_name,
                                      user=user,
                                      password=password
                                      )
        
        cursor = connection.cursor()

        """Create tables in the database"""

        statements = (
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            password VARcHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            address VARCHAR(255) NOT NULL,
            telephone VARCHAR(255) NOT NULL,
            admin BOOLEAN NOT NULL
        )
        """,
        """ CREATE TABLE status (
                status_id SERIAL PRIMARY KEY,
                status_name VARCHAR(255) NOT NULL
            )
        """,
        """
        CREATE TABLE menus (
                menu_id SERIAL PRIMARY KEY,
                meal_name VARCHAR(255) NOT NULL UNIQUE,
                quantity INTEGER NOT NULL,
                description VARCHAR(255) NOT NULL,
                cost INTEGER NOT NULL
            )
        """,
        """
        CREATE TABLE orders (
                order_id SERIAL,
                total_cost INT NOT NULL,
                status_table_id INT REFERENCES status(status_id) ON DELETE CASCADE,
                PRIMARY KEY (order_id, status_table_id)
            )
        """)

        for statement in statements:
            cursor.execute(statement)
        
        cursor.close()
   
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Erroe connecting", error)

    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


    if __name__ == '__main__':
        connection_to_main()