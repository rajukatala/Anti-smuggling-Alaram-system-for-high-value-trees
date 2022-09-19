from machine import Pin, I2C
import network
import time
import uumail
from umqtt.robust import MQTTClient
import paho.mqtt.client as mqtt
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
    wifi.connect('oppo','1234567891998')
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
            connect_wifi()
            weather_data = requests.get(open_weather_map_url)
            wind = 'Wind: ' + str(weather_data.json().get('wind').get('speed')) 
            print(wind)
            time.sleep(2)
            if(wind>='5'):
                smtp = uumail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
                smtp.login('rkatala1998@gmail.com', 'zaijiiazfzypvixj')
                smtp.to('rajuramkatala@gmail.com')
                smtp.write("From: Security <rkatala1998@gmail.com>\n")
                smtp.write("To: Farmar <rajuramkatala@gmail.com>\n")
                smtp.write("Subject: Alert!Thief detected in our farm.\n\n")
                smtp.write("Wind speed is avrage so there definatly thirg in our farm.(Parent node)\n")
                smtp.write("Please check.\n")
                smtp.write("...\n")
                smtp.send()
                smtp.quit()
                print('Mail sent')
                req = urequests.post('https://maker.ifttt.com/trigger/{Alert}/json/with/key/cNZ-LUAK8Cg8IYSDzJhmx')
                print('notification send')
                req.close()
            else:
                smtp = uumail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
                smtp.login('rkatala1998@gmail.com', 'zaijiiazfzypvixj')
                smtp.to('rajuramkatala@gmail.com')
                smtp.write("From: Security <rkatala1998@gmail.com>\n")
                smtp.write("To: Farmar <rajuramkatala@gmail.com>\n")
                smtp.write("Subject: Alert!Thief detected in our farm.\n\n")
                smtp.write("Wind speed is High so there may be theif or not in our farm.\n")
                smtp.write("Please check.\n")
                smtp.write("...\n")
                smtp.send()
                smtp.quit()
                print('Mail sent')
                req = urequests.post('https://maker.ifttt.com/trigger/{Alert}/json/with/key/cNZ-LUAK8Cg8IYSDzJhmx')
                print('notification send')
                req.close()


broker_url = "192.268.43.253"
broker_port = 8080
x=0
x =  message.payload.decode()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_url, broker_port)

client.subscribe("test_topic", qos=2)




#client.loop_forever()
while True:
    
     senser()
     if(x==0): 
         wifi = network.WLAN(network.AP_IF)
         wifi.active(True)
         wifi.config(essid='ESP',authmode=network.AUTH_WPA_WPA2_PSK, password='password')
#          print(wifi.ifconfig())
      else:
         connect_wifi()
         if(x==1)
            smtp = uumail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
            smtp.login('rkatala1998@gmail.com', 'zaijiiazfzypvixj')
            smtp.to('rajuramkatala@gmail.com')
            smtp.write("From: Security <rkatala1998@gmail.com>\n")
            smtp.write("To: Farmar <rajuramkatala@gmail.com>\n")
            smtp.write("Subject: Alert!Thief detected in our farm.\n\n")
            smtp.write("Wind speed is avrage so there definatly thirg in our farm.(chils node)\n")
            smtp.write("Please check.\n")
            smtp.write("...\n")
            smtp.send()
            smtp.quit()
            print('Mail sent')
            req = urequests.post('https://maker.ifttt.com/trigger/{Alert}/json/with/key/cNZ-LUAK8Cg8IYSDzJhmx')
            print('notification send')
            req.close()
         if else(x==2)
               smtp = uumail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
                smtp.login('rkatala1998@gmail.com', 'zaijiiazfzypvixj')
                smtp.to('rajuramkatala@gmail.com')
                smtp.write("From: Security <rkatala1998@gmail.com>\n")
                smtp.write("To: Farmar <rajuramkatala@gmail.com>\n")
                smtp.write("Subject: Alert!Thief detected in our farm.\n\n")
                smtp.write("Wind speed is High so there may be theif or not in our farm(child node).\n")
                smtp.write("Please check.\n")
                smtp.write("...\n")
                smtp.send()
                smtp.quit()
                print('Mail sent')
                req = urequests.post('https://maker.ifttt.com/trigger/{Alert}/json/with/key/cNZ-LUAK8Cg8IYSDzJhmx')
                print('notification send')
                req.close()


         
     
     
    


