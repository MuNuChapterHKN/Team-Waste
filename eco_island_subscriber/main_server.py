#!/usr/bin/python3

import paho.mqtt.client as mqtt
import data_access.volume_sensor_data_access as vsda
import data_access.bin_data_access as bda
import data_access.sensor_data_access as sda
import data_access.load_sensor_data_access as lsda
import data_access.infrared_sensor_data_access as isda

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    messaggio = str(message.payload.decode("utf-8"))
    #IDEAL FORMAT: bin_id SENSOR_ID timestamp samp --> separati da tab
    fields = messaggio.split(" ")
    print(fields)

    sensor_id = fields[0]
    # timestamp = fields[1]
    measured_value = fields[2]
    # bin id and type of the sensor
    sensor = sda.get_sensor(sensor_id)
    bin_id = sensor['bin_id']
    sensor_type = sensor['type']
    # get island id given the bin id
    island_id = bda.get_bin_island_id(bin_id)
    # save into db according to type
    if sensor_type == 1:
        isda.add_measurement_value(bin_id, island_id, measured_value)
    elif sensor_type == 2:
        lsda.add_measurement_value(bin_id, island_id, measured_value)
    elif sensor_type == 3:
        vsda.add_measurement_value(bin_id, island_id, measured_value)
    else:
        print("undefined sensor type")
    

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















