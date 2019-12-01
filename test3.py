import tkinter as tk
import pygubu
import paho.mqtt.client as mqtt

class Application:
    def __init__(self, master):
        self.master = master
        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('mainInterface_0.2.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('mainwindow', master)
        builder.connect_callbacks(self)

    def quit_click(self):
        self.master.quit()
    def prog1_click(self):
        print("program1")

class Page1:
    def __init__(self, master):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('mainInterface_0.2.ui')
        self.mainwindow = builder.get_object('prog1_window', master)
        builder.connect_callbacks(self)
    def returnhome(self):
        print("retyurn home")

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Application, Page1):

            frame = F(container)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Application)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



if __name__ == '__main__':
    mqttc = mqtt.Client()
    mqttc.connect("localhost", 1883, 60)
    mqttc.subscribe("$SYS/#", 0)
    # root = tk.Tk()
    # app = Application(root)
    # root.mainloop()
    app = SeaofBTCapp()
    app.mainloop()