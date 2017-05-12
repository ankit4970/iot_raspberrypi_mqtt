#! /usr/bin/env python3

import paho.mqtt.client as mqtt
import MySQLdb
import time

# Define Variables
MQTT_BROKER = "iot.eclipse.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "cmpe297/sensor"
temperature =0.0
lat = 37.336082
lon = -121.882572
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
	#print(msg)
	var = (msg.payload.decode())
	print(var)
	var1=var.split(',')
	for words in var1:
		print(words)
	datetime = time.strftime("%m/%d/%Y")
	localtime = time.asctime( time.localtime(time.time()) )
	print("Local current time :", localtime)
	try:
		lat =(float)(var1[0])
		lon=(float)(var1[1])
		temp =(float)(var1[2])
		# Execute the SQL command
		cursor.execute("INSERT INTO sensordata (lat,lon,temperature,datetime) values (%f,%f,%f,'%s')" %(lat,lon,temp,localtime))
   		# Commit your changes in the database
		db.commit()
	except:
		# Rollback in case there is any error
		db.rollback()

# Open database connection
db = MySQLdb.connect("localhost","root","root","sensor" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "INSERT INTO sensordata (lat,lon,temperature,datetime) values (%f,%f,%f,'%s')" %(lat,-121.8863290,29.89,"05/10/2017")

client = mqtt.Client()
client.connect(MQTT_BROKER,MQTT_PORT,MQTT_KEEPALIVE_INTERVAL )

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

