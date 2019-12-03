import os
import signal
import subprocess
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/sub")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if(str(msg.payload) == "b'p1'"):
        # process = subprocess.Popen(['python3', 'hworld.py'])
        process1 = subprocess.run(["python3", "hworld.py"])
        # time.sleep(5)
        # process.terminate()
    if(str(msg.payload) == "b'qp1'"):
        process = subprocess.Popen(['python3', 'hworld.py'])
        time.sleep(5)
        process.terminate()
    if(str(msg.payload) == "b'p2'"):
        process = subprocess.Popen(['python3', 'hworld.py'])
    elif(str(msg.payload) == "b'qp2"):
        process.kill()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("jlmbp.local", 1883, 60)

client.loop_forever()