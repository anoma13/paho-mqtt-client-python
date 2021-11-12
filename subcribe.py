import paho.mqtt.client as mqtt
import time

message = ""
topic = "sister"

def on_message(client, userdata, message):
    message = str(message.payload.decode("utf-8"))
    print("message received ", message)
    message_received = True
    
connected = False
message_received = False
broker_address = "192.168.1.20"

client = mqtt.Client("MQTT")
client.on_message = on_message
time.sleep(1.5)
print("connecting to", broker_address)
i = 1
while i < 4:
    time.sleep(1)
    print(".")
    i += 1
print("conneted")
client.connect(broker_address, port=1883)

client.loop_start()
client.subscribe(topic)

while connected != True or message_received != True:
    time.sleep(0.2)

client.loop_forever()
