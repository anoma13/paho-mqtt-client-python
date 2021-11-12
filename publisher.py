import paho.mqtt.client as mqtt
import time

connected = False
broker_address = "192.168.1.20"

client = mqtt.Client("P1") 
#client.on_connect = on_connect
time.sleep(1.5)
print("conneted to",broker_address)
client.connect(broker_address)
client.loop_start()

time.sleep(1)
topic = input("Topic:")
message = input("Message:")

time.sleep(2)
while True:    
    client.publish(topic,message)
    print("Publishing... ",message)
    time.sleep(4)
