from tkinter import *
from tkinter.ttk import*
screen = Tk()
screen.geometry("300x100")
bar = Progressbar(screen,orient=HORIZONTAL,length=200,mode="determinate")
bar.pack()
screen.mainloop()
