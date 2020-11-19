import sqlite3
from mysql.connector import Error

def check_database(connection,filename):
	conn = sqlite3.connect(filename)
	c = conn.cursor()
	if c.fetchone()[0]==1 : 
		print('Database exists.')
	else :
		print('Database does not exist.')
		query = "CREATE DATABASE EPICS_project"
		create_database(connection, query)
		
def create_database(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		print("Database created successfully")
	except Error as err:
		print(f"Error: '{err}'")
