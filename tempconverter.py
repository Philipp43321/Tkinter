from tkinter import *
import tkinter.font as font
screen = Tk()
screen.geometry("500x300")

#function for conversion
def converter():
    unconv = text.get()
    if (unconv.replace('.','',1).isdigit()):
        errormessage.place_forget()
        conv = float(unconv)*(9/5) + 32
        outputtext.config(text="Temperature in farenheit: "+str(conv))
    else:
        errormessage.config(text="Please enter a valid number")
        errormessage.place(x=280,y=95)


titletext = Label(screen,text="Celsius -> Farenheit",font=font.Font(size=20),fg="black").place(x=120,y=10)
inputtitle = Label(screen,text="Enter temperature in celsius:",font=font.Font(size=15),fg="gray").place(x=30,y=70)
outputtext = Label(screen,font=font.Font(size=15),fg="gray")
outputtext.place(x=50,y=120)
errormessage = Label(screen,font=font.Font(size=8),fg="red")

button = Button(screen,text="CONVERT",width=10,fg="black",bg="lime",command=converter).place(x=200,y=200)
text = Entry(screen,width=20)
text.place(x=290,y=75)


screen.mainloop()
