
import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("esp32/sensor")

def on_message(client, userdata, msg):
  print(msg)
  if msg.payload.decode() == "disconnect":
    client.disconnect()
    
    
    
client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()