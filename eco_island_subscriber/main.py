#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:06:23 2020

@author: andreatiloca
"""
import paho.mqtt.client as mqtt
import sqlite3
import mysql.connector
from mysql.connector import Error
import pandas as pd

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))
def on_publish(client, obj, mid):
    print("mid: " + str(mid))

# -----------------------------------------------------------------------
# Qui prima va inserita la parte di creazione della connessione al server
# -----------------------------------------------------------------------

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

#Funzione che controlla la presenza di un database e in caso non esistesse lo crea
database = ch_data.check_database(connection,"EPICS_project")

#Inscrizione al topic
a = mqtt.subscribe("esp32/sensor", 0)

conn = sqlite3.connect('EPICS_project.db')
c = conn.cursor()

#Funzione in cui aggiungo il messaggio in coda alla tabella e crea la tabella nel caso 
#non fosse presente
add_messagge = tabella.check_table(c,msg,connection)
