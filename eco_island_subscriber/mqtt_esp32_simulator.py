#!/usr/bin/python3

import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("esp32/sensor", "01 01 120320201220 23")
client.disconnect()