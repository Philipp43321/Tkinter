from tkinter import*
from tkinter.ttk import*
#retrieving system time
from time import strftime
screen = Tk()
screen.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    clock.config(text=string)
    clock.after(1000,time)

clock = Label(screen,font=("arial",120),background="blue",foreground="black")
clock.pack(anchor="center")
time()
screen.mainloop()