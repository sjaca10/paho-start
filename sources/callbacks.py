import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
	print("Connected with result code " + str(rc))
	client.subscribe("hello/kliento")

def on_disconnect(client, userdata, rc):
	client.unsubscribe("hello/kliento")
	if rc != 0:
		print("Unexpected disconnection [" + str(rc) + "]")
	else:
		print("Disconnection with result code " + str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribing " + str(client) + " to topic ?")

def on_unsubscribe(client, userdata, mid):
	print("Unsubscribing " + str(client) + " from topic ?")

def on_message(client, userdata, msg):
	print("Recibiendo mensaje")
	print(msg.topic + " " + str(msg.payload))

def on_publish(client, userdata, mid):
	print("Message publish, completed transmition to the broker")

def on_log(client, userdata, level, buf):
	print("Level " + str(level) + " Buffer: " + str(buf))

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_unsubscribe = on_unsubscribe
client.on_message = on_message
client.on_publish = on_publish
client.on_log = on_log

client.connect("45.55.210.26", 1883, 60)
client.publish("hello/kliento", payload = "Hello everybody from procedural!", qos = 0, retain = False)
client.loop_forever()
client.disconnect()