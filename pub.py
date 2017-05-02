#! /usr/bin/env python3
import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()
mqttc.connect("localhost", 1883)
mqttc.publish("hello/world", "Hello, World!")

while True:
	mqttc.publish("hello/world", "Hello, World!")
	time.sleep(1)

mqttc.loop_forever() 									#timeout = 2s
