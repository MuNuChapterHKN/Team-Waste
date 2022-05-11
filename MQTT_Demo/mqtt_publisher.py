import paho.mqtt.client as mqtt
#pip install paho-mqtt
# This is the Publisher

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

client = mqtt.Client()
client.username_pw_set('publisher','publisher')

client.connect("192.168.1.12",1883,60)
client.publish("topic/test", "Hello world!")
client.disconnect()