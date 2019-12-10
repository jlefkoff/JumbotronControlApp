import tkinter as tk
import paho.mqtt.client as mqtt
from PIL import Image, ImageTk
import time

mqttc = mqtt.Client()
mqttc.connect('mqttbroker')

LARGE_FONT= ("Verdana", 25)
SMALL_FONT= ("Verdana", 30)


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.grid(row=0,column=0)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        mqttc = mqtt.Client()
        mqttc.connect('mqttbroker')

        for F in (StartPage, Prog1, Prog2, Prog3, Prog4, Prog5):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        global mqttc
        mqttc.publish('test/sub', payload='startup')

        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Hello! What program would you like to run?", font=LARGE_FONT)
        label.grid(row=0,column=0, columnspan=2)

        button = tk.Button(self, text="Snake Game",
                            command=lambda:[controller.show_frame(Prog1), mqttc.publish("shutdown"), mqttc.publish('test/sub', payload="p1")], font=SMALL_FONT)
        button.grid(row=1,column=0, ipadx=140)

        button2 = tk.Button(self, text="Audio Visualizer",
                            command=lambda:[controller.show_frame(Prog2), mqttc.publish("shutdown"), mqttc.publish('test/sub', payload='p2'), mqttc.publish('test/sub', payload='p2b')], font=SMALL_FONT)
        button2.grid(row=2,column=0, ipadx=140)

        button3 = tk.Button(self, text="Donut Color Picker",
                            command=lambda:[controller.show_frame(Prog3), mqttc.publish("shutdown"), mqttc.publish('test/sub', payload='p3')], font=SMALL_FONT)
        button3.grid(row=3,column=0, ipadx=140)

        button4 = tk.Button(self, text="Light Cycles",
                            command=lambda:[controller.show_frame(Prog4), mqttc.publish("shutdown"), mqttc.publish('test/sub', payload='p4')], font=SMALL_FONT)
        button4.grid(row=4,column=0, ipadx=140, sticky="s")
        button4 = tk.Button(self, text="Camera",
                            command=lambda:[controller.show_frame(Prog5), mqttc.publish("shutdown"), mqttc.publish('test/sub', payload='p5'), mqttc.publish('test/sub', payload='p5b')], font=SMALL_FONT)
        button4.grid(row=5,column=0, ipadx=140, sticky="s")



class Prog1(tk.Frame):

    def __init__(self, parent, controller):
        global mqttc
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To control this program -1, visit: \n example.com", font=LARGE_FONT, height=3)
        label.grid(row=0,column=0, columnspan=2)

        load = Image.open("qrcode.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1,column=0, columnspan=2)

        button1 = tk.Button(self, text="Quit Program",
                            command=lambda: [controller.show_frame(StartPage), mqttc.publish('test/sub', payload='qp1'), mqttc.publish('test/sub', payload='startup')], font=SMALL_FONT)
        button1.grid(row=2,column=0, columnspan=2)


class Prog2(tk.Frame):

    def __init__(self, parent, controller):
        global mqttc
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To control this program -2, visit: \n example.com", font=LARGE_FONT, height=3)
        label.grid(row=0,column=0, columnspan=2)

        load = Image.open("qrcode.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1,column=0, columnspan=2)

        button1 = tk.Button(self, text="Quit Program",
                            command=lambda: [controller.show_frame(StartPage), mqttc.publish('test/sub', payload='qp2'), time.sleep(1), mqttc.publish('test/sub', payload='startup')], font=SMALL_FONT)
        button1.grid(row=2,column=0, columnspan=2)

        
class Prog3(tk.Frame):

    def __init__(self, parent, controller):
        global mqttc
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To control this program -3, visit: \n example.com", font=LARGE_FONT, height=3)
        label.grid(row=0,column=0, columnspan=2)

        load = Image.open("qrcode.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1,column=0, columnspan=2)

        button1 = tk.Button(self, text="Quit Program",
                            command=lambda: [controller.show_frame(StartPage), mqttc.publish('test/sub', payload='qp3'), time.sleep(1), mqttc.publish('test/sub', payload='startup')], font=SMALL_FONT)
        button1.grid(row=2,column=0, columnspan=2)
        
class Prog4(tk.Frame):

    def __init__(self, parent, controller):
        global mqttc
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To control this program -4, visit: \n example.com", font=LARGE_FONT, height=3)
        label.grid(row=0,column=0, columnspan=2)

        load = Image.open("qrcode.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1,column=0, columnspan=2)

        button1 = tk.Button(self, text="Quit Program",
                            command=lambda: [controller.show_frame(StartPage), mqttc.publish('test/sub', payload='qp4'), time.sleep(1), mqttc.publish('test/sub', payload='startup')], font=SMALL_FONT)
        button1.grid(row=2,column=0, columnspan=2)

class Prog5(tk.Frame):
    
    def __init__(self, parent, controller):
        global mqttc
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To control this program -5, visit: \n example.com", font=LARGE_FONT, height=3)
        label.grid(row=0,column=0, columnspan=2)

        load = Image.open("qrcode.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1,column=0, columnspan=2)

        button1 = tk.Button(self, text="Quit Program",
                            command=lambda: [controller.show_frame(StartPage), mqttc.publish('test/sub', payload='qp5'), time.sleep(1), mqttc.publish('test/sub', payload='startup')], font=SMALL_FONT)
        button1.grid(row=2,column=0, columnspan=2)

        


app = MainApp()
app.mainloop()