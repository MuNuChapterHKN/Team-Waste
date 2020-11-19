import mysql.connector
from mysql.connector import Error

def check_table(c,msg):	
	#get the count of tables with the name
	c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='data_epics' ''')
	#if the count is 1, then table exists
	if c.fetchone()[0]==1 : 
		print('Table exists.')
		pop_table = msg
		execute_query(connection, pop_table)
	else :
		print('Table does not exist.')
		create_table_EPICS = """
		CREATE TABLE data_epics (
			bin_id VARCHAR(40) NOT NULL,
			time_stamp VARCHAR(40) NOT NULL,
			sample VARCHAR(40) NOT NULL
			);
			"""
		connection = create_db_connection("localhost", "root", pw, db) # Connect to the Database
		execute_query(connection, create_table_EPICS) # Execute our defined query
		pop_table = msg
		c.execute("INSERT INTO `EPICS_project`.`data_epics` (message)VALUES (%s)",(pop_table)) 

		
def execute_query(connection, query):
	cursor = connection.cursor()
	try:
		#ricontrolla query inserimento dato
		cursor.execute(query)
		connection.commit()
		print("Query successful")
	except Error as err:
		print(f"Error: '{err}'") 
def create_db_connection(host_name, user_name, user_password, db_name):
	connection = None
	try:
		connection = mysql.connector.connect(
			host=host_name,
			user=user_name,
			passwd=user_password,
			database=db_name
		)
		print("MySQL Database connection successful")
	except Error as err:
		print(f"Error: '{err}'")
