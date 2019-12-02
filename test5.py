import tkinter as tk
import paho.mqtt.client as mqtt
from PIL import Image, ImageTk


LARGE_FONT= ("Verdana", 25)
SMALL_FONT= ("Verdana", 35)


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        #container.pack(side="top", fill="both", expand = True)
        container.grid(row=0,column=0)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        mqttc = mqtt.Client()
        mqttc.connect('jlmbp.local')

        for F in (StartPage, Prog1, Prog2, Prog3, Prog4):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        mqttc = mqtt.Client()
        mqttc.connect('jlmbp.local')
        mqttc.publish('test/sub', payload='startup')

        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Hello! What program would you like to run?", font=LARGE_FONT)
        label.grid(row=0,column=0, columnspan=2)

        button = tk.Button(self, text="Run Program 1",
                            command=lambda:[controller.show_frame(Prog1), print("running program 1"), mqttc.publish('test/sub', payload='run program 1')], font=SMALL_FONT)
        button.grid(row=1,column=0, ipadx=140)

        button2 = tk.Button(self, text="Run Program 2",
                            command=lambda: controller.show_frame(Prog2), font=SMALL_FONT)
        button2.grid(row=2,column=0, ipadx=140)

        button3 = tk.Button(self, text="Run Program 3",
                            command=lambda: controller.show_frame(Prog3), font=SMALL_FONT)
        button3.grid(row=3,column=0, ipadx=140)

        button4 = tk.Button(self, text="Run Program 4",
                            command=lambda: controller.show_frame(Prog4), font=SMALL_FONT)
        button4.grid(row=4,column=0, ipadx=140, sticky="s")



class Prog1(tk.Frame):

    def __init__(self, parent, controller):
        mqttc = mqtt.Client()
        mqttc.connect('jlmbp.local')
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To control this program, visit: \n example.com", font=LARGE_FONT, height=3)
        label.grid(row=0,column=0, columnspan=2)

        load = Image.open("qrcode.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=1,column=0)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage), font=SMALL_FONT)
        button1.grid(row=2,column=0)

        button2 = tk.Button(self, text="send mqtt command",
                            command=lambda: mqttc.publish('test/sub', payload='p1'), font=SMALL_FONT)
        button2.grid(row=2,column=1)


class Prog2(tk.Frame):

    def __init__(self, parent, controller):
        mqttc = mqtt.Client()
        mqttc.connect('jlmbp.local')
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To control this program, visit: \n example.com", font=LARGE_FONT, height=3)
        label.grid(row=0,column=0, columnspan=2)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage), font=SMALL_FONT)
        button1.grid(row=1,column=0)

        button2 = tk.Button(self, text="send mqtt command",
                            command=lambda: mqttc.publish('test/sub', payload='p2'), font=SMALL_FONT)
        button2.grid(row=1,column=1)
        
class Prog3(tk.Frame):

    def __init__(self, parent, controller):
        mqttc = mqtt.Client()
        mqttc.connect('jlmbp.local')
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To control this program, visit: \n example.com", font=LARGE_FONT, height=3)
        label.grid(row=0,column=0, columnspan=2)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage), font=SMALL_FONT)
        button1.grid(row=1,column=0)

        button2 = tk.Button(self, text="send mqtt command",
                            command=lambda: mqttc.publish('test/sub', payload='p3'), font=SMALL_FONT)
        button2.grid(row=1,column=1)
        
class Prog4(tk.Frame):

    def __init__(self, parent, controller):
        mqttc = mqtt.Client()
        mqttc.connect('jlmbp.local')
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To control this program, visit: \n example.com", font=LARGE_FONT, height=3)
        label.grid(row=0,column=0, columnspan=2)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage), font=SMALL_FONT)
        button1.grid(row=1,column=0)

        button2 = tk.Button(self, text="send mqtt command",
                            command=lambda: mqttc.publish('test/sub', payload='p4'), font=SMALL_FONT)
        button2.grid(row=1,column=1)
        


app = MainApp()
app.mainloop()