from machine import Pin, I2C
import network
import time
import uumail
from umqtt.robust import MQTTClient
import paho.mqtt.client as mqtt
#import paho.mqtt as mq
try:
  import urequests as requests
except:
  import requests

import ADXL3445
import esp

esp.osdebug(None)

import ujson as json

import gc
gc.collect()

def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.disconnect()
    wifi.connect('esp','password')
    if not wifi.isconnected():
        print('connecting..')
        timeout = 0
        while (not wifi.isconnected() and timeout < 5):
            print(5 - timeout)
            timeout = timeout + 1
            time.sleep(1) 
    if(wifi.isconnected()):
        print('connected')
    else:
        print('not connected')
def  senser():
    url = "172.20.43.39"
    port = 1883
    topic = "test_topic"
    client = mqtt.Client()
    client.connect(url, port)
    city = 'Allahabad'
    country_code = 'IN'
    i2c = I2C(scl=Pin(22),sda=Pin(21), freq=10000)
    adx = ADXL3445.ADXL345(i2c)

    open_weather_map_api_key = '6d6ca359b7e46f1c18c19122b905afbd'
    while True:
        x=adx.xValue
        y=adx.yValue
        z=adx.zValue
        print('The acceleration info of x, y, z are:%d,%d,%d'%(x,y,z))
        open_weather_map_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + country_code + '&APPID=' + open_weather_map_api_key

        if(x>=65 or y>=65 or z>=260):
            #connect_wifi()
            weather_data = requests.get(open_weather_map_url)
            wind = 'Wind: ' + str(weather_data.json().get('wind').get('speed')) #+ 'mps '   #+ str(weather_data.json().get('wind').get('deg')) + '*'
            print(wind)
            time.sleep(2)
            if(wind>='5'):
                client.publish(topic, payload=1, qos=2, retain=False)
                time.sleep(1)

            else:
                client.publish(topic, payload=2, qos=2, retain=False)
                time.sleep(1)




broker_url = "192.268.43.253"
broker_port = 8080 
  x =  message.payload.decode()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_url, broker_port)

client.subscribe("test_topic", qos=2)




#client.loop_forever()
while True:
     connect_wifi()
     senser()
     
         
     
     
    


