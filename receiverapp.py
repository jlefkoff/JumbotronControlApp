import paho.mqtt.client as mqtt
import os
import subprocess
import time

class makeProcess:
    def make(self, arg1, arg2):
        self.internalProcess = subprocess.Popen([arg1,arg2])
    def kill(self):
        self.internalProcess.kill()
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/sub")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if(str(msg.payload) == "b'p1'"):
        # os.system("python3 hworld.py")
        mainProcess.make('python3','hworld.py')
        time.sleep(5)
    elif(str(msg.payload) == "b'qp1'"):
        mainProcess.kill()
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

mainProcess = makeProcess()

client.connect("jlmbp.local", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()