from tkinter import *
from tkinter.ttk import*
screen = Tk()
screen.geometry("300x100")
bar = Progressbar(screen,orient=HORIZONTAL,length=200,mode="determinate")
bar.pack()
def progress():
    import time
    bar["value"]=20
    screen.update_idletasks()
    time.sleep(1)

    bar["value"]=40
    screen.update_idletasks()
    time.sleep(1)
    
    bar["value"]=60
    screen.update_idletasks()
    time.sleep(1)

    bar["value"]=80
    screen.update_idletasks()
    time.sleep(1)

    bar["value"]=100

button = Button(screen,text="Press Me",command=progress)
button.pack()

#spinbox
spinbox=Spinbox(screen,from_=0,to=20)
spinbox.pack()
screen.mainloop()
