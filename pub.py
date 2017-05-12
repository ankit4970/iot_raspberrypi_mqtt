#! /usr/bin/env python3
import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()
mqttc.connect("iot.eclipse.org", 1883)
mqttc.publish("cmpe297/sensor", "Hello, World!")

while True:
	buf="27.83,728.3,34.3,05/17/2017"
	mqttc.publish("cmpe297/sensor", buf)
	time.sleep(1)

mqttc.loop_forever() 									#timeout = 2s
