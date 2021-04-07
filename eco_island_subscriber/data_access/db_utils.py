import mysql.connector
from mysql.connector import Error

config = {
  'user': 'root',
  'password': 'Mkg-18691948!', #'Rumapark97',
  'host': '127.0.0.1',
  'database': 'threekeco',
  'raise_on_warnings': True
}

def create_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**config)
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def execute_insert_query(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Insert Query successful")
        cursor.close()
    except Error as err:
        print(f"Error: '{err}'") 

def execute_select_one_query(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = None
        result = cursor.fetchone()        
        print("Select One Query successful")
        cursor.close()
        return result
    except Error as err:
        print(f"Error: '{err}'") 

def execute_select_many_query(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = []
        result = cursor.fetchall()        
        print("Select Many Query successful")
        cursor.close()
        return result
    except Error as err:
        print(f"Error: '{err}'") 

connection = create_db_connection()