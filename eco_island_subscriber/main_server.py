import mysql.connector
from mysql.connector import Error
import pandas as pd
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    messaggio = str(message.payload.decode("utf-8"))
    #IDEAL FORMAT: bin_id SENSOR_ID timestamp samp --> separati da tab
    fields = messaggio.split(" ")
    print(fields)
    add_to_table = f"""
    INSERT INTO epics_table (bin_id,sensor_id,timestamp,samp) VALUES ({fields[0]},{fields[1]},{fields[2]},{fields[3]});
    """
    connection = create_db_connection("localhost", "root", "Rumapark97", "Epics_project") # Connect to the Database
    execute_query(connection, add_to_table) # Execute our defined query

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")     

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

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

    return connection

connection = create_server_connection("localhost", "root", "Rumapark97") # Connect to the serve
query = "CREATE DATABASE IF NOT EXISTS Epics_project"
create_database(connection, query)
connection = create_db_connection("localhost", "root", "Rumapark97", "Epics_project") # Directly connect to the database


create_epics_table = """
      CREATE TABLE IF NOT EXISTS epics_table (
      bin_id  int NOT NULL PRIMARY KEY,
      sensor_id  int NOT NULL PRIMARY KEY,
      timestamp VARCHAR(40) NOT NULL PRIMARY KEY,
      samp VARCHAR(40)
      );
    """
        #cerca mysqu timestamp formato

execute_query(connection, create_epics_table) # Execute our defined query


broker_address="localhost"  #qua va inserito l'indirizzo ip del broker 

print("creating new instance")
client = mqtt.Client() #create new instance

print("connecting to broker")
client.connect(broker_address,port=1883,keepalive=60) #connect to broker
# keepalive: se il broker non risponde dopo deltaT, chiudi
client.subscribe("esp32/sensor") # connessione al topic su cui pubblica il client
# qua va inserirto il topic a cui iscrivere il SUBSCRIBER

client.on_message=on_message #leggo il messaggio arrivato dal broker
#e lo inserisco in tabella

# e rimango in attesa fino allo stop del programma
client.loop_forever()















