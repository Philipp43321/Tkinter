from tkinter import*
from tkinter.ttk import*
#retrieving system time
from time import strftime
screen = Tk()
screen.title("Clock")


clock = Label(screen,font=("arial",120),text="12:56:23",background="blue",foreground="black")
clock.pack(anchor="center")
screen.mainloop()