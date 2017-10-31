from network import WLAN 
import mqtt 
import machine 
import time 
 
def sub_cb(topic, msg): 
   print(msg) 
 
wlan = WLAN(mode=WLAN.STA) 
wlan.connect("WiFiname", auth=(WLAN.WPA2, "WiFipassword"), timeout=5000) 
 
while not wlan.isconnected():  
    machine.idle() 
print("Connected to Wifi\n") 
 
client = MQTTClient("device_id", "io.adafruit.com",user="username", password="AIO key", port=1883) 
client.set_callback(sub_cb) 
client.connect()
client.subscribe(topic="username/feeds/lights") 
while True: 
    print("Sending ON") 
    client.publish(topic="username/feeds/lights", msg="ON")

    time.sleep(1) 
    print("Sending OFF") 
    client.publish(topic="username/feeds/lights", msg="OFF")
    
    time.sleep(1) 
    
    
    
#In this project, "WiFiname" and "WiFipassword" mean the name and password of the WiFi which your computer is connecting right now, not the information of WiPy board.
#In this case, I use the "io.adafruit.com" as the middlewire to receive the message of WiPy board. 
#The username and AIO key can be gain in "io.adafruit.com".
#"lights" is the name of "Feed" I established in my adafruit account. You can change it.
#Most of the information is got from  https://www.hackster.io/bucknalla/mqtt-micropython-044e77?ref=channel&ref_id=13739_trending___&offset=1
#I also modified some places. If I invade the authority, please tell me soon.
