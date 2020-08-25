import paho.mqtt.client as mqtt
import os.path

mqtt_server_host = "192.168.0.17"
mqtt_server_port = "1883"
mqtt_keepalive = 60

def on_connect(client, userdata, rc):
	print("Connect result: {}".format(mqtt.connack_string(rc)))

def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribed with QoS: {}".format(granted_qos[0]))

def on_message(client, userdata, msg):
	payload_string = msg.payload.decode('utf-8')
	print("Topic: {}, payload: {}".format(msg.topic, payload_string))

if __name__ == "__main__":
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_subscribe = on_subscribe
	client.on_message = on_message

	client.connect(host=mqtt_server_host, port=mqtt_server_port, keepalive=mqtt_keepalive)
	client.subscribe("#")
	client.loop_forever()
