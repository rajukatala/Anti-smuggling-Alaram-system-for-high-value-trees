This project implements a safety-alarm system for high-value trees on farms by the Internet of Things concept using micro-controllers such as the Esp32 devkit v1 and communication protocols
 such as MQTT within the network. In this one tree has what is called the Parent/Co-ordinator node which is like the gateway for the entire network's information and alerts communicating 
to the farmer. 
         In the default/normal/safe situation, the whole network is not connected to the internet. The parent node acts an Wifi-access point for the rest of the network and all other 
         nodes connect to it as Wifi-stations. An MQTT broker called mosquitto runs on the parent node and all others connect to it as clients using the umqtt client software. 
         The parent node must be attached to that tree that is most closest to the WiFi router.

         Acceleration sensors present on each node continously measure the vibration/shaking of the tree. Acceleration above a threshold triggers the node to publish to the parent node 
        that there has been a possible attack on it. The parent node then switches it's mode into a Station and makes an API call to OpenWeather.com and retrieves the wind speed from it. 
        Based on the wind speed, the parent node will now send both an e-mail to the farmer's mail address and in case the farmer also downloaded the IFTTT app on his mobile, he'll also 
        get the push-notification on his mobile about the possible attack on that particular tree and the wind condition. For the push-notification, the parent node sends a numeric code 
        based on the wind speed and the tree under attack to an IFTTT web applet running on their cloud platform and the notification information is sent accordingly.

This project folder contains 2 main codes, 
1) pr_main.py to be run on the Parent/Co-ordinator node 
2) ch_main.py on all the other nodes of the network.
Note: Rename both files as main.py before uploading them to the esp32.

          Other module codes included are the ADXL345.py library file which needs to be uploaded to every board/node on the network , the umail.py library file only on the 
         parent/co-ordinator node.
An active Wi-Fi connection must be there on-site for the parent-node to be able to send mail cum notifications to the farmer's mobile and make API calls to o btain the weather data. 