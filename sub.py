#! /usr/bin/env python3

import paho.mqtt.client as mqtt
import MySQLdb


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("hello/world")

def on_message(client, userdata, msg):
	print(msg.payload.decode())
	try:
		# Execute the SQL command
		cursor.execute(sql)
   		# Commit your changes in the database
		db.commit()
	except:
		# Rollback in case there is any error
		db.rollback()

# Open database connection
db = MySQLdb.connect("localhost","root","root","mysql" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = """INSERT INTO sensorData (lat,lon,temperature,datetime) values (37.3382080,-121.8863290,5,4)"""

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

