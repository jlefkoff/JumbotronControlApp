import gi
import paho.mqtt.client as mqtt

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

icons = ["edit-cut", "edit-paste", "edit-copy"]

broker="localhost"
port=1883

def on_publish(client,userdata,result):#create function for callback
    print("data published \n")
    pass

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.button1 = Gtk.Button(label="Click to activate button 1")
        self.button1.connect("clicked", self.on_button_clicked)
        self.add(self.button1)
        self.button2 = Gtk.Button(label="click to activate program 2")
        self.button2.connect("clicked", self.on_button_clicked)
        self.add(self.button2)



    def on_button_clicked(self, widget):
        ret= client1.publish("set/test","on")
        print("yo")

client1 = mqtt.Client("control1")  #create client object
client1.on_publish = on_publish #assign function to callback
client1.connect(broker,port)        #establish connection
#publish

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()