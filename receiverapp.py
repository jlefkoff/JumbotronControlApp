import paho.mqtt.client as mqtt
import os
import subprocess
import time

class makeProcess:
    def makeMe(self, arg1, arg2):
        self.internalProcess = subprocess.Popen(['sudo',arg1,arg2])
        print("Process spawned with PID: %s" % self.internalProcess.pid)
        self.pgid = os.getpgid(internalProcess.pid)
    def killMe(self):
        self.internalProcess.terminate()
        # subprocess.run('kill -s ' + self.internalProcess.pid)
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/sub")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # if(str(msg.payload == "b'startup'")):
    #     backProcess.makeMe('python','/home/pi/git_repos/fish_tank/space_tank.py')
    # elif(str(msg.payload == "b'close_startup'")):
    #     backProcess.killMe()
    if(str(msg.payload) == "b'p1'"):
        # os.system("python3 hworld.py")
        mainProcess.makeMe('python','/home/pi/glenn/mqtt_gamepad/wormgame_mqtt.py')
        #time.sleep(5)
    elif(str(msg.payload) == "b'qp1'"):
        print("kill received p1")
        client.publish("shutdown")
    elif(str(msg.payload) == "b'p2'"):
        mainprocess2.makeMe('python','/home/pi/glenn/audio_mqtt/dual_display.py')
    elif(str(msg.payload) == "b'p2b'"):
        mainProcess.makeMe('python','/home/pi/glenn/audio_mqtt/mic_full.py')
    elif(str(msg.payload) == "b'qp2'"):
        print("kill received p2")
        client.publish("shutdown")
    elif(str(msg.payload) == "b'p3'"):
        mainProcess.makeMe('python','/home/pi/glenn/temp/DonutsMQTT.py')
    elif(str(msg.payload) == "b'qp3'"):
        print("kill received p3")
        client.publish("shutdown")
    elif(str(msg.payload) == "b'p4'"):
        mainProcess.makeMe('python','/home/pi/glenn/mqtt_gamepad/cycles_4p.py')
    elif(str(msg.payload) == "b'qp4'"):
        print("kill received p4")
        client.publish("shutdown")
    elif(str(msg.payload) == "b'p5'"):
        mainProcess.makeMe('python','/home/pi/glenn/mqtt_camera/camera_mqtt.py')
    elif(str(msg.payload) == "b'p5b'"):
        mainProcess.makeMe('python','/home/pi/glenn/mqtt_camera/display_mqtt.py')
    elif(str(msg.payload) == "b'qp5'"):
        print("kill received p5")
        client.publish("shutdown")

    


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

backProcess = makeProcess()
mainProcess = makeProcess()
mainprocess2 = makeProcess()

client.connect("mqttbroker", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()