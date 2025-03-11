from tkinter import *
import tkinter.font as font
screen = Tk()
screen.geometry("500x300")

titletext = Label(screen,text="Celsius -> Farenheit",font=font.Font(size=20),fg="black").place(x=120,y=10)
inputtitle = Label(screen,text="Enter temperature in celsius:",font=font.Font(size=15),fg="gray").place(x=30,y=70)
outputtext = Label(screen,font=font.Font(size=15),fg="gray")
errormessage = Label(screen,font=font.Font(size=12,fg="red"))
button = Button(screen,text="CONVERT",width=100,fg="black",bg="lime")
button.pack()


screen.mainloop()