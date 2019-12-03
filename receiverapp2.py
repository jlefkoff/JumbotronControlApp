import os
import signal
import subprocess
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/sub")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if(str(msg.payload) == "p1"):
        pro = subprocess.Popen(['echo','hello'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                       shell=True, preexec_fn=os.setsid) 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("jlmbp.local", 1883, 60)


# The os.setsid() is passed in the argument preexec_fn so
# it's run after the fork() and before  exec() to run the shell.
stdout, stderr = pro.communicate()
print(stdout)
os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # Send the signal to all the process groups