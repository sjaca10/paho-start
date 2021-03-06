import paho.mqtt.client as mqtt

class CompanyClient(mqtt.Client):

	def on_connect(self, client, userdata, rc):
		print("Connected with result code " + str(rc))
		client.subscribe("hello/company")

	def on_subscribe(self, client, userdata, mid, granted_qos):
		print("Subscribing " + str(client) + " to the topic ?")

	def on_message(self, client, userdata, msg):
		print(msg.topic + " " + str(msg.payload))

	def on_publish(self, client, userdata, mid):
		print("Message publish, completed transmition to the broker")

client = CompanyClient()

client.connect("localhost", 1883, 60)

client.publish("hello/company", payload = "Hello everybody from POO!", qos = 0, retain = False)

client.loop_forever()