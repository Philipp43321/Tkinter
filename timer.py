from tkinter import*
import time
from tkinter import messagebox
screen = Tk()
screen.geometry("300x130")

h = StringVar()
m = StringVar()
s = StringVar()
h.set("00")
m.set("00")
s.set("00")

hour = Entry(screen,width=5,font=("arial",20),textvariable=h)
hour.place(x=20,y=20)
minute = Entry(screen,width=5,font=("arial",20),textvariable=m)
minute.place(x=110,y=20)
second = Entry(screen,width=5,font=("arial",20),textvariable=s)
second.place(x=200,y=20)

def converter():
    try:
        hms = int(hour.get())*3600+int(minute.get())*60+int(second.get())
    except:
        print("invalid input")
    while hms > -1:
        min,sec = divmod(hms,60)
        hr = 00
        if min > 60:
            hr,min = divmod(min,60)
        h.set("{00:2d}".format(hr))
        m.set("{00:2d}".format(min))
        s.set("{00:2d}".format(sec))
        screen.update()
        time.sleep(1)
        if hms == 0:
            messagebox.showinfo("TIME IS UP","TIME IS UP")
        hms -= 1


button = Button(screen,text="START",bd=5,command=converter)
button.place(x=110,y=70)

screen.mainloop()