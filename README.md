# iot_raspberrypi_mqtt
# On Raspberry Pi

	pi@raspberrypi:~ $ sudo apt-get update
	pi@raspberrypi:~ $ sudo apt-get install php5 libapache2-mod-php5 -y
	pi@raspberrypi:~ $ sudo apt-get install php5-mysql
	pi@raspberrypi:~ $ sudo pip3 install paho-mqtt

#	 Install and start mosquitto broker
	pi@raspberrypi:~ $ sudo apt-get install mosquitto
	pi@raspberrypi:~ $ systemctl status mosquitto


#	Mysql Commands

	pi@raspberrypi:~ $ sudo apt-get install python-pip python-dev libmysqlclient-dev
	pi@raspberrypi:~ $ sudo apt-get install python-mysqldb
	pi@raspberrypi:~ $ sudo apt-get install mysql-python
	pi@raspberrypi:~ $ pip3 install mysqlclient
	pi@raspberrypi:~ $ pip3 install MySQL-python

	pi@raspberrypi:~ $ mysql -u root -p
	mysql> show databases;
	mysql> use test;
	mysql> select * from sensorData;
	mysql> insert into sensorData (lat,lon,temperature,datetime) values (37.3382080,-121.8863290,5);
	mysql> select * from sensorData;
	mysql> select * from sensorData;

	pi@raspberrypi:~ $ python3 pub.py
	pi@raspberrypi:~ $ python3 sub.py

