# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

import tkinter as tk


LARGE_FONT= ("Verdana", 40)
SMALL_FONT= ("Verdana", 30)


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        #container.pack(side="top", fill="both", expand = True)
        container.grid(row=0,column=0)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Prog1, Prog2):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT, padx=150, pady=100)
        label.grid(row=0,column=0, columnspan=2)

        button = tk.Button(self, text="Run Program 1",
                            command=lambda: controller.show_frame(Prog1), font=SMALL_FONT)
        button.grid(row=1,column=0)

        button2 = tk.Button(self, text="Run Program 2",
                            command=lambda: controller.show_frame(Prog2), font=SMALL_FONT)
        button2.grid(row=1,column=1)



class Prog1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To control this program, visit: \n example.com", font=LARGE_FONT)
        label.grid(row=0,column=0, columnspan=2)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage), font=SMALL_FONT)
        button1.grid(row=1,column=0)

        button2 = tk.Button(self, text="Say yo!",
                            command=lambda: print("yo"), font=SMALL_FONT)
        button2.grid(row=1,column=1)


class Prog2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To control this program, visit: \n example.com", font=LARGE_FONT)
        label.grid(row=0,column=0, columnspan=2)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage), font=SMALL_FONT)
        button1.grid(row=1,column=0)

        button2 = tk.Button(self, text="Print Hey",
                            command=lambda: print("hey"), font=SMALL_FONT)
        button2.grid(row=1,column=1)
        


app = MainApp()
app.mainloop()