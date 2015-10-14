import paho.mqtt.client as mqtt

class KlientoClient(mqtt.Client):

	def on_connect(self, client, userdata, rc):
		print("Connected with result code " + str(rc))
		client.subscribe("hello/kliento")

	def on_subscribe(self, client, userdata, mid, granted_qos):
		print("Subscribing " + str(client) + " to the topic ?")

	def on_message(self, client, userdata, msg):
		print(msg.topic + " " + str(msg.payload))

	def on_publish(self, client, userdata, mid):
		print("Message publish, completed transmition to the broker")

client = KlientoClient()

client.connect("45.55.210.26", 1883, 60)

client.publish("hello/kliento", payload = "Hello everybody from POO!", qos = 0, retain = False)

client.loop_forever()