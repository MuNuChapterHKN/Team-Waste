
import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
    client.disconnect()

#it must be called before connect in order to see its effects
def set_authentication_params(client,username,password):
  client.username_pw_set('subscriber','subscriber')

client = mqtt.Client()

set_authentication_params(client,'subscriber','subscriber')
client.connect("192.168.1.12",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()